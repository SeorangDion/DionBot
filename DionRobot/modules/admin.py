from DionRobot import dion
from DionRobot.status import *

from telethon import events, Button
from telethon.tl.functions.channels import EditAdminRequest, EditBannedRequest
from telethon.tl.types import ChatAdminRights, ChatBannedRights
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import ExportChatInviteRequest


ADMIN_TEXT = """
**✘ A module from which admins of the chat can use!**
‣ `/ban` - To ban a user in the chat.
‣ `/kick` - To kick a user in the chat.
‣ `/promote` - To Promote a user in the chat.
‣ `/demote` - To Demote a user in the chat.
‣ `/invitelink` - To get invitelink of a chat.
"""

@dion.on(events.callbackquery.CallbackQuery(data="admin"))
async def _(event):
    await event.edit(ADMIN_TEXT, buttons=[[Button.inline("« Bᴀᴄᴋ", data="help")]])

@dion.on(events.NewMessage(pattern="^[!?/]promote ?(.*)"))
@is_admin
async def promote(event, perm):
    if event.is_private:
       await event.reply("This cmd is made to be used in groups, not in PM!")
       return

    if not perm.add_admins:
        await event.reply("You are missing the following rights to use this command:__Can Add Admins!__")
        return
    input_str = event.pattern_match.group(1)
    user = await event.get_reply_message()
    if not input_str and not user:
        await event.reply("Reply to a user or give its username to promote him!")
        return
    sed = await dion(GetFullUserRequest(id=user.sender_id or input_str))
    await dion(EditAdminRequest(event.chat_id, user.sender_id or input_str, ChatAdminRights(
                    add_admins=False,
                    invite_users=True,
                    change_info=False,
                    ban_users=True,
                    delete_messages=True,
                    pin_messages=True), rank="Admin"))

    if not input_str:
        await event.reply(f"Successfully Promoted [{sed.user.first_name}](tg://user?id={user.sender_id}) in {event.chat.title}!")
        return

    await event.reply(f"Succesfully Promoted {input_str} in {event.chat.title}")
 
@dion.on(events.NewMessage(pattern="^[!?/]demote ?(.*)"))
@is_admin
async def demote(event, perm):
    if event.is_private:
       await event.reply("This cmd is made to be used in groups, not in PM!")
       return
    if not perm.add_admins:
        await event.reply("You are missing the following rights to use this command:__Can Add Admins!__")
        return
    input_str = event.pattern_match.group(1)
    user = await event.get_reply_message()
    if not input_str and not user:
        await event.reply("Reply to a user or give its username to demote him!")
        return
    sed = await dion(GetFullUserRequest(id=user.sender_id or input_str))
    await dion(EditAdminRequest(event.chat_id, user.sender_id or input_str, ChatAdminRights(
                    add_admins=False,
                    invite_users=None,
                    change_info=None,
                    ban_users=None,
                    delete_messages=None,
                    pin_messages=None), rank="Not Admin"))

    if not input_str:
        await event.reply(f"Successfully Demoted [{sed.user.first_name}](tg://user?id={user.sender_id}) in {event.chat.title}!")
        return

    await event.reply(f"Succesfully Demoted {input_str} in {event.chat.title}")
 

@dion.on(events.NewMessage(pattern="^[!?/]kick ?(.*)"))
@is_admin
async def kick(event, perm):
    if event.is_private:
        await event.reply("This cmd is made to be used in groups not PM")
        return
    if not perm.ban_users:
         await event.reply("You are missing the following rights to use this command:__Can Ban Users!__")
         return
    input_str = event.pattern_match.group(1)
    msg = await event.get_reply_message()
    if not input_str and not msg:
        await event.reply("Reply to a user or give its username to kick him")
        return

    replied_user = msg.sender_id
    us = msg.sender.username
    info = await dion.get_entity(us)
    await dion.kick_participant(event.chat_id, input_str or replied_user)
    await event.reply(f"Succesfully Kicked [{info.first_name}](tg://user?id={replied_user}) from {event.chat.title}")


@dion.on(events.NewMessage(pattern="^[!?/]ban ?(.*)"))
@is_admin
async def ban(event, perm):
    if event.is_private:
        await event.reply("This cmd is made to be used in groups not PM")
        return
    if not perm.ban_users:
        await event.reply("You are missing the following rights to use this command:__Can Ban Users!__")
        return
    input_str = event.pattern_match.group(1)
    msg = await event.get_reply_message()
    if not input_str and not msg:
        await event.reply("Reply to a user or give its username to ban him")
        return
    replied_user = msg.sender_id
    us = msg.sender.username
    info = await dion.get_entity(us)
    await dion(EditBannedRequest(event.chat_id, replied_user, ChatBannedRights(until_date=None, view_messages=True)))
    await event.reply(f"Succesfully Banned [{info.first_name}](tg://user?id={replied_user}) in {event.chat.title}")


@dion.on(events.NewMessage(pattern="^[!?/]invitelink"))
async def invitelink(event):

    if event.is_private:
       await event.reply("This cmd is made to be used in groups, not in PM!")
       return
    link = await dion(ExportChatInviteRequest(event.chat_id))
    await event.reply(f"Group link of {event.chat.title} is [here]({link.link})", link_preview=False)
