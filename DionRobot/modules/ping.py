import time
from datetime import datetime

from .. import dion
from telethon import events

StartTime = time.time()

def get_readable_time(seconds: int) -> str:
    count = 0
    timer = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        timer += time_list.pop() + ", "
    time_list.reverse()
    timer += ":".join(time_list)

    return timer


@dion.on(events.NewMessage(pattern="^[?!/]ping ?(.*)"))
async def _ping(event):
    uptime = get_readable_time((time.time() - StartTime))
    start = datetime.now()
    msg = await event.reply("`Pinging...`")
    end = datetime.now()
    ping = (end - start).microseconds / 1000
    await msg.edit(
         "PONG!!!\n"
        f"**Ping**: `{ping} ms`\n"
        f"**Uptime**: `{uptime}`"
    )
