from telethon import events, Button
from telethon import __version__ as tlhver

from DionRobot import dion

ABOUT_TXT = f"""
👋🏼 **Hi, I'm Dion Robot**

💠 I'm Working Properly 

💠 Python Version : `3.10.4` 

💠 Telethon Version : `{tlhver}`

Thanks For Using Me.
"""


BTN = [[Button.url("Updates", "https://t.me/DionProjects"), Button.url("Support", "https://t.me/DionSupport")]]


@dion.on(events.NewMessage(pattern="^[!?/]about ?(.*)"))
async def lock(event):
    await event.reply(ABOUT_TXT, buttons=BTN)
 
