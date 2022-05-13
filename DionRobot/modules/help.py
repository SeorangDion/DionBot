from telethon import events, Button
from DionRobot import dion

btn =[
    [Button.inline("Admin", data="admin"), Button.inline("Bans", data="bans")],
    [Button.inline("Pins", data="pins"), Button.inline("Pugres", data="purges")],
    [Button.inline("Locks", data="locks"), Button.inline("Misc", data="misc")],
    [Button.inline("Chat Cleaner", data="zombies")]]

HELP_TEXT = """
**Dion Robot help menu:**

/start - To Start Me ;)
/help - To Get Available Help Menu
/donate - Donate me :)

__Report Bugs At--->__ @DionSupport
All cmd can be used with '/' or '!'.
"""


@dion.on(events.NewMessage(pattern="[!?/]help"))
async def help(event):
    if event.is_group:
       await event.reply("Contact me in PM to get available help menu!", 
       buttons=[
       [Button.url("Help And Commands!", "https://t.me/DionRobot?start=help")]])
       return

    await event.reply(HELP_TEXT, buttons=btn)

@dion.on(events.NewMessage(pattern="^/start help"))
async def shelp(event):
    await event.reply(HELP_TEXT, buttons=btn)


@dion.on(events.callbackquery.CallbackQuery(data="help"))
async def chelp(event):
     await event.edit(HELP_TEXT, buttons=btn)
