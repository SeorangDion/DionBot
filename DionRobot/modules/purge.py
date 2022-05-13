import time

from telethon import events, Button
from DionRobot import dion
from DionRobot.status import *

PURGE_TEXT = """
**✘ Need to delete lots of messages? That's what purges are for!**
‣ `/purge` - Reply to a msg to delete msgs from there.
‣ `/spurge` - Same as purge, but doesnt send the final confirmation message.
‣ `/del` - Deletes the replied to message.
"""

@dion.on(events.NewMessage(pattern=r"^[?/!]purge"))
@is_admin
async def purge_messages(event, perm):
    if not perm.delete_messages:
         await event.reply("You are missing the following rights to use this command: __Can Delete Message!__")
         return
    start = time.perf_counter()
    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.reply(
            "Reply to a message to select where to start purging from.")
        return
    messages = []
    message_id = reply_msg.id
    delete_to = event.message.id

    messages.append(event.reply_to_msg_id)
    for msg_id in range(message_id, delete_to + 1):
        messages.append(msg_id)
        if len(messages) == 100:
            await event.client.delete_messages(event.chat_id, messages)
            messages = []

    await event.client.delete_messages(event.chat_id, messages)
    time_ = time.perf_counter() - start
    text = f"Purged in {time_:0.2f} Second(s)"
    await event.respond(text, parse_mode='markdown')

@dion.on(events.NewMessage(pattern="^[!?/]spurge"))
@is_admin
async def spurge(event, perm):
    if not perm.delete_messages:
         await event.reply("You are missing the following rights to use this command:__Can Delete Message!__")
         return
    start = time.perf_counter()
    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.reply(
            "Reply to a message to select where to start purging from.")
        return
    messages = []
    message_id = reply_msg.id
    delete_to = event.message.id

    messages.append(event.reply_to_msg_id)
    for msg_id in range(message_id, delete_to + 1):
        messages.append(msg_id)
        if len(messages) == 100:
            await event.client.delete_messages(event.chat_id, messages)
            messages = []

    await event.client.delete_messages(event.chat_id, messages)

@dion.on(events.NewMessage(pattern="^[!?/]del$"))
@dion.on(events.NewMessage(pattern="^[!?/]delete$"))
@is_admin
async def delete_messages(event, perm):
    if not perm.delete_messages:
       await event.reply("You are missing the following rights to use this command:__Can Delete Message!__")
       return
    msg = await event.get_reply_message()
    if not msg:
      await event.reply("Reply to a msg to delete it.")
      return

    await msg.delete()
    await event.delete()

@dion.on(events.callbackquery.CallbackQuery(data="purges"))
async def _(event):
    await event.edit(PURGE_TEXT, buttons=[[Button.inline("« Bᴀᴄᴋ", data="help")]])
