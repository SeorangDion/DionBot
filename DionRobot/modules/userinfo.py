from DionRobot import dion
from DionRobot.status import *

from telethon import events, Button, types
from telethon.tl.types import ChannelParticipantsAdmins
from datetime import timedelta
from telethon.tl.functions.photos import GetUserPhotosRequest as P
from telethon.tl.functions.users import GetFullUserRequest


MISC_HELP = """
**✘ An "odds and ends" module for small, simple commands which don't really fit anywhere.**
‣ `/id` - To get current chat id or replied user id.
‣ `/info` - To get info of a user.
"""

@dion.on(events.NewMessage(pattern="^[!?/]id ?(.*)"))
async def id(event):

    if event.is_private:
       await event.reply(f"❏ **Your ID**:\n└ `{event.sender_id}`.")
       return

    ID = """
**Your ID:** `{}`
**Group ID:** `{}`
"""

    msg = await event.get_reply_message()
    if not msg:
      await event.reply(ID.format(event.sender_id, event.chat_id))
      return

    await event.reply(f"❏ **{msg.sender.first_name} ID**:\n└ `{msg.sender_id}`.\n\n❏ **Group's ID**:\n└ `{event.chat_id}`")
 
@dion.on(events.NewMessage(pattern="^[!?/]info ?(.*)"))
async def info(event):

    sed = await dion(P(user_id=event.sender_id, offset=42, max_id=0, limit=80))
    ion = await dion(GetFullUserRequest(event.sender_id))
    text = "**✘ UserInfo:**\n\n"
    text += "**» Fɪʀsᴛ Nᴀᴍᴇ:** {}\n"
    text += "**» Lᴀsᴛ Nᴀᴍᴇ:** {}\n"
    text += "**» Usᴇʀ-ID:** `{}`\n"
    text += "**» Usᴇʀɴᴀᴍᴇ:** @{}\n"
    text += "**» Nᴏ. Oғ Pғᴘs:** `{}`\n"
    text += "**» Usᴇʀ-Bɪᴏ:** `{}`\n"
    text += "**» PᴇʀᴍᴀLɪɴᴋ:** [Link](tg://user?id={})\n"

    input_str = event.pattern_match.group(1)
    if not input_str:
          await dion.send_message(event.chat_id, text.format(ion.user.first_name, ion.user.last_name, event.sender_id, event.sender.username, sed.count, ion.about, event.sender_id))
          return
 
    input_str = event.pattern_match.group(1)
    deon = await dion.get_entity(input_str)
    on = await dion(GetFullUserRequest(id=input_str))
    sedd = await dion(P(user_id=input_str, offset=42, max_id=0, limit=80))

    textn = "**✘ UserInfo:**\n\n"
    textn += "**» Fɪʀsᴛ Nᴀᴍᴇ:** {}\n"
    textn += "**» Lᴀsᴛ Nᴀᴍᴇ:** {}\n"
    textn += "**» Usᴇʀ-ID:** `{}`\n"
    textn += "**» Usᴇʀɴᴀᴍᴇ:** @{}\n"
    textn += "**» Nᴏ. Oғ Pғᴘs:** `{}`\n"
    textn += "**» Usᴇʀ-Bɪᴏ:** `{}`\n"
    textn += "**» PᴇʀᴍᴀLɪɴᴋ:** [Link](tg://user?id={})\n"

    await event.reply(textn.format(deon.first_name, deon.last_name, deon.id, deon.username, sedd.count, on.about, deon.id))
   

@dion.on(events.callbackquery.CallbackQuery(data="misc"))
async def _(event):
    await event.edit(MISC_HELP, buttons=[[Button.inline("« Bᴀᴄᴋ", data="help")]])
