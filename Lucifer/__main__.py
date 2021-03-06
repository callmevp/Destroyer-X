import glob
from pathlib import Path
from sys import argv

import telethon.utils
from telethon import TelegramClient

from Lucifer import CMD_HNDLR, bot
from Lucifer.LuciferConfig import Var
from Lucifer.utils import load_module, load_pmbot, start_mybot

LION = Var.PRIVATE_GROUP_ID
BOTNAME = Var.TG_BOT_USER_NAME_BF_HER
LOAD_MYBOT = Var.LOAD_MYBOT


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


async def startup_log_all_done():
    try:
        await bot.send_message(
            LION,
            f"**LUCIFER π±πΎπ πΈπ π³π΄πΏπ»πΎππ΄π³.\nππ΄π½π³** `{CMD_HNDLR}alive` **ππΎ ππ΄π΄ π±πΎπ πΈπ ππΎππΊπΈπ½πΆ πΎπ π½πΎπ.\n\nAdd** @{BOTNAME} **π°π³π³ ππΎ ππ·πΈπ πΈπ½ ππΎππ πΆππΎππΏ π°π½π³ πΌπ°πΊπ΄ π·πΈπΌ π°π³πΌπΈπ½ π΅πΎπ π΄π½π°π±π»πΈπ½πΆ π°π»π» ππ·π΄ π΅π΄π°ππππ΄π πΎπ΅ LUCIFER π±πΎπ**",
        )
    except BaseException:
        print("Either PRIVATE_GROUP_ID is wrong or you have left the group.")


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()

path = "Lucifer/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

print("Lucifer has been deployed! ")

print("Setting up TGBot")
path = "Lucifer/plugins/mybot/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        start_mybot(shortname.replace(".py", ""))

if LOAD_MYBOT == "True":
    path = "Lucifer/plugins/mybot/pmbot/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            load_pmbot(shortname.replace(".py", ""))
    print("TGBot set up completely!")

print("TGBot set up - Level - Basic")
print(
    """
                ----------------------------------------------------------------------
                    LUCIFER X Κα΄s Κα΄α΄Ι΄ α΄α΄α΄Κα΄Κα΄α΄, α΄α΄ α΄ ΙͺsΙͺα΄ @Lucifer_support_group !!
                    LUCIFER α΄ α΄Κ: V2.2
                    Β©Tα΄α΄α΄ Κuifer
                ----------------------------------------------------------------------
"""
)
bot.loop.run_until_complete(startup_log_all_done())

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
