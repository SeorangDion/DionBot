import glob
import logging

from pathlib import Path
from DionRobot.utils import load_plugins
from DionRobot import dion

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

path = "DionRobot/modules/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
    
dion_txt = "Any questions? Say it at t.me/DionSupport\n"
dion_txt += "Bot started! Maintaned by Dion"
print(dion_txt)

if __name__ == "__main__":
    dion.run_until_disconnected()
