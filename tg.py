from telethon import TelegramClient, events, sync
import os,time
from colorama import Fore
from telethon.tl.functions.messages import GetHistoryRequest 

file=open(".api_id", "r")
api_id= (file.read())
file.close
file=open(".api_hash", "r")
api_hash= (file.read())
file.close
if api_id==(""):
  api_id=input("введіть api_id: ")
  file=open(".api_id", "w")
  file.write(api_id)
  file.close()
if api_hash==(""):
  api_hash=input("введіть api_hash: ")
  file=open(".api_hash", "w")
  file.write(api_hash)
  file.close()
def cls():
    os.system("clear")

client = TelegramClient("session_name", api_id, api_hash)

client.start()
konec=input (Fore.GREEN+"надпис в кінці >>> "+Fore.WHITE)
cls()

z = 1
@client.on(events.NewMessage(pattern=('heart❤️')))
async def edit(event):
  await event.edit("""✨✨✨💓💓✨✨✨💓💓✨✨✨
✨✨💓💓💓💓✨💓💓💓💓✨✨
✨💓💓💓💓💓💓💓💓💓💓💓✨
✨💓💓💓💓💓💓💓💓💓💓💓✨
✨💓💓💓💓💓💓💓💓💓💓💓✨
✨✨💓💓💓💓💓💓💓💓💓✨✨
✨✨✨💓💓💓💓💓💓💓✨✨✨
✨✨✨✨💓💓💓💓💓✨✨✨✨
✨✨✨✨✨💓💓💓✨✨✨✨✨
✨✨✨✨✨✨💓✨✨✨✨✨✨""")
  time.sleep(0.2)
  await event.edit("""✨✨✨💓💓✨✨✨💓💓✨✨✨
✨✨💓💓💓💓✨💓💓💓💓✨✨
✨💓💓💓💓💓💓💓💓💓💓💓✨
✨💓💓💓💓💓💓💓💓💓💓💓✨
✨💓💓💓💓💓💓💓💓💓💓💓✨
✨✨💓💓💓💓💓💓💓💓💓✨✨
✨✨✨💓💓💓💓💓💓💓✨✨✨
✨✨✨✨💓💓💓💓💓✨✨✨✨
✨✨✨✨✨💓💓💓✨✨✨✨✨
✨✨✨✨✨✨😍✨✨✨✨✨✨""")
  time.sleep(0.2)
  await event.edit("""✨✨✨💓💓✨✨✨💓💓✨✨✨
✨✨💓💓💓💓✨💓💓💓💓✨✨
✨💓💓💓💓💓💓💓💓💓💓💓✨
✨💓💓💓💓💓💓💓💓💓💓💓✨
✨💓💓💓💓💓💓💓💓💓💓💓✨
✨✨💓💓💓💓💓💓💓💓💓✨✨
✨✨✨💓💓💓💓💓💓💓✨✨✨
✨✨✨✨💓💓💓💓💓✨✨✨✨
✨✨✨✨✨😍💓😍✨✨✨✨✨
✨✨✨✨✨✨😍✨✨✨✨✨✨""")
  time.sleep(0.2)
  await event.edit("""✨✨✨💓💓✨✨✨💓💓✨✨✨
✨✨💓💓💓💓✨💓💓💓💓✨✨
✨💓💓💓💓💓💓💓💓💓💓💓✨
✨💓💓💓💓💓💓💓💓💓💓💓✨
✨💓💓💓💓💓💓💓💓💓💓💓✨
✨✨💓💓💓💓💓💓💓💓💓✨✨
✨✨✨💓💓💓💓💓💓💓✨✨✨
✨✨✨✨😍💓💓💓😍✨✨✨✨
✨✨✨✨✨😍💓😍✨✨✨✨✨
✨✨✨✨✨✨😍✨✨✨✨✨✨""")
  time.sleep(0.2)
  await event.edit("""✨✨✨💓💓✨✨✨💓💓✨✨✨
✨✨💓💓💓💓✨💓💓💓💓✨✨
✨💓💓💓💓💓💓💓💓💓💓💓✨
✨💓💓💓💓💓💓💓💓💓💓💓✨
✨💓💓💓💓💓💓💓💓💓💓💓✨
✨✨💓💓💓💓💓💓💓💓💓✨✨
✨✨✨😍💓💓💓💓💓😍✨✨✨
✨✨✨✨😍💓💓💓😍✨✨✨✨
✨✨✨✨✨😍💓😍✨✨✨✨✨
✨✨✨✨✨✨😍✨✨✨✨✨✨""")
  time.sleep(0.2)
  await event.edit("""✨✨✨💓💓✨✨✨💓💓✨✨✨
✨✨💓💓💓💓✨💓💓💓💓✨✨
✨💓💓💓💓💓💓💓💓💓💓💓✨
✨💓💓💓💓💓💓💓💓💓💓💓✨
✨💓💓💓💓💓💓💓💓💓💓💓✨
✨✨😍💓💓💓💓💓💓💓😍✨✨
✨✨✨😍💓💓💓💓💓😍✨✨✨
✨✨✨✨😍💓💓💓😍✨✨✨✨
✨✨✨✨✨😍💓😍✨✨✨✨✨
✨✨✨✨✨✨😍✨✨✨✨✨✨""")
  time.sleep(0.2)
  await event.edit("""✨✨✨💓💓✨✨✨💓💓✨✨✨
✨✨💓💓💓💓✨💓💓💓💓✨✨
✨💓💓💓💓💓💓💓💓💓💓💓✨
✨💓💓💓💓💓💓💓💓💓💓💓✨
✨😍💓💓💓💓💓💓💓💓💓😍✨
✨✨😍💓💓💓💓💓💓💓😍✨✨
✨✨✨😍💓💓💓💓💓😍✨✨✨
✨✨✨✨😍💓💓💓😍✨✨✨✨
✨✨✨✨✨😍💓😍✨✨✨✨✨
✨✨✨✨✨✨😍✨✨✨✨✨✨""")
  time.sleep(0.2)
  await event.edit("""✨✨✨💓💓✨✨✨💓💓✨✨✨
✨✨💓💓💓💓✨💓💓💓💓✨✨
✨💓💓💓💓💓💓💓💓💓💓💓✨
✨😍💓💓💓💓💓💓💓💓💓😍✨
✨😍💓💓💓💓💓💓💓💓💓😍✨
✨✨😍💓💓💓💓💓💓💓😍✨✨
✨✨✨😍💓💓💓💓💓😍✨✨✨
✨✨✨✨😍💓💓💓😍✨✨✨✨
✨✨✨✨✨😍💓😍✨✨✨✨✨
✨✨✨✨✨✨😍✨✨✨✨✨✨""")
  time.sleep(0.2)
  await event.edit("""✨✨✨💓💓✨✨✨💓💓✨✨✨
✨✨💓💓💓💓✨💓💓💓💓✨✨
✨😍💓💓💓💓💓💓💓💓💓😍✨
✨😍💓💓💓💓💓💓💓💓💓😍✨
✨😍💓💓💓💓💓💓💓💓💓😍✨
✨✨😍💓💓💓💓💓💓💓😍✨✨
✨✨✨😍💓💓💓💓💓😍✨✨✨
✨✨✨✨😍💓💓💓😍✨✨✨✨
✨✨✨✨✨😍💓😍✨✨✨✨✨
✨✨✨✨✨✨😍✨✨✨✨✨✨""")
  time.sleep(0.2)
  await event.edit("""✨✨✨💓💓✨✨✨💓💓✨✨✨
✨✨😍💓💓💓✨💓💓💓😍✨✨
✨😍💓💓💓💓💓💓💓💓💓😍✨
✨😍💓💓💓💓💓💓💓💓💓😍✨
✨😍💓💓💓💓💓💓💓💓💓😍✨
✨✨😍💓💓💓💓💓💓💓😍✨✨
✨✨✨😍💓💓💓💓💓😍✨✨✨
✨✨✨✨😍💓💓💓😍✨✨✨✨
✨✨✨✨✨😍💓😍✨✨✨✨✨
✨✨✨✨✨✨😍✨✨✨✨✨✨""")
  time.sleep(0.2)
  await event.edit("""✨✨✨😍💓✨✨✨💓😍✨✨✨
✨✨😍💓💓💓✨💓💓💓😍✨✨
✨😍💓💓💓💓💓💓💓💓💓😍✨
✨😍💓💓💓💓💓💓💓💓💓😍✨
✨😍💓💓💓💓💓💓💓💓💓😍✨
✨✨😍💓💓💓💓💓💓💓😍✨✨
✨✨✨😍💓💓💓💓💓😍✨✨✨
✨✨✨✨😍💓💓💓😍✨✨✨✨
✨✨✨✨✨😍💓😍✨✨✨✨✨
✨✨✨✨✨✨😍✨✨✨✨✨✨""")
  time.sleep(0.2)
  await event.edit("""✨✨✨😍😍✨✨✨😍😍✨✨✨
✨✨😍💓💓💓✨💓💓💓😍✨✨
✨😍💓💓💓💓💓💓💓💓💓😍✨
✨😍💓💓💓💓💓💓💓💓💓😍✨
✨😍💓💓💓💓💓💓💓💓💓😍✨
✨✨😍💓💓💓💓💓💓💓😍✨✨
✨✨✨😍💓💓💓💓💓😍✨✨✨
✨✨✨✨😍💓💓💓😍✨✨✨✨
✨✨✨✨✨😍💓😍✨✨✨✨✨
✨✨✨✨✨✨😍✨✨✨✨✨✨""")
  time.sleep(0.2)
  await event.edit("""✨✨✨😍😍✨✨✨😍😍✨✨✨
✨✨😍💓💓😍✨😍💓💓😍✨✨
✨😍💓💓💓💓💓💓💓💓💓😍✨
✨😍💓💓💓💓💓💓💓💓💓😍✨
✨😍💓💓💓💓💓💓💓💓💓😍✨
✨✨😍💓💓💓💓💓💓💓😍✨✨
✨✨✨😍💓💓💓💓💓😍✨✨✨
✨✨✨✨😍💓💓💓😍✨✨✨✨
✨✨✨✨✨😍💓😍✨✨✨✨✨
✨✨✨✨✨✨😍✨✨✨✨✨✨""")
  time.sleep(0.2)
  await event.edit("""✨✨✨😍😍✨✨✨😍😍✨✨✨
✨✨😍💓💓😍✨😍💓💓😍✨✨
✨😍💓💓💓💓😍💓💓💓💓😍✨
✨😍💓💓💓💓💓💓💓💓💓😍✨
✨😍💓💓💓💓💓💓💓💓💓😍✨
✨✨😍💓💓💓💓💓💓💓😍✨✨
✨✨✨😍💓💓💓💓💓😍✨✨✨
✨✨✨✨😍💓💓💓😍✨✨✨✨
✨✨✨✨✨😍💓😍✨✨✨✨✨
✨✨✨✨✨✨😍✨✨✨✨✨✨""")
  time.sleep(0.2)
  await event.edit("""✨✨✨😍😍✨✨✨😍😍✨✨✨
✨✨😍😍😍😍✨😍😍😍😍✨✨
✨😍😍💓💓😍😍😍💓💓😍😍✨
✨😍😍💓💓💓😍💓💓💓😍😍✨
✨😍😍💓💓💓💓💓💓💓😍😍✨
✨✨😍😍💓💓💓💓💓😍😍✨✨
✨✨✨😍😍💓💓💓😍😍✨✨✨
✨✨✨✨😍😍💓😍😍✨✨✨✨
✨✨✨✨✨😍😍😍✨✨✨✨✨
✨✨✨✨✨✨😍✨✨✨✨✨✨""")
  time.sleep(0.2)
  await event.edit("""✨✨✨😍😍✨✨✨😍😍✨✨✨
✨✨😍😍😍😍✨😍😍😍😍✨✨
✨😍😍😍😍😍😍😍😍😍😍😍✨
✨😍😍😍💓💓😍💓💓😍😍😍✨
✨😍😍😍💓💓💓💓💓😍😍😍✨
✨✨😍😍😍💓💓💓😍😍😍✨✨
✨✨✨😍😍😍💓😍😍😍✨✨✨
✨✨✨✨😍😍😍😍😍✨✨✨✨
✨✨✨✨✨😍😍😍✨✨✨✨✨
✨✨✨✨✨✨😍✨✨✨✨✨✨""")
  time.sleep(0.2)
  await event.edit("""✨✨✨😍😍✨✨✨😍😍✨✨✨
✨✨😍😍😍😍✨😍😍😍😍✨✨
✨😍😍😍😍😍😍😍😍😍😍😍✨
✨😍😍😍😍😍😍😍😍😍😍😍✨
✨😍😍😍😍😍😍😍😍😍😍😍✨
✨✨😍😍😍😍😍😍😍😍😍✨✨
✨✨✨😍😍😍😍😍😍😍✨✨✨
✨✨✨✨😍😍😍😍😍✨✨✨✨
✨✨✨✨✨😍😍😍✨✨✨✨✨
✨✨✨✨✨✨😍✨✨✨✨✨✨""")
  time.sleep(0.2)
  await event.edit("""✨✨✨🌹🌹✨✨✨🌹🌹✨✨✨
✨✨🌹🌹🌹🌹✨🌹🌹🌹🌹✨✨
✨🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹✨
✨🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹✨
✨🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹✨
✨✨🌹🌹🌹🌹🌹🌹🌹🌹🌹✨✨
✨✨✨🌹🌹🌹🌹🌹🌹🌹✨✨✨
✨✨✨✨🌹🌹🌹🌹🌹✨✨✨✨
✨✨✨✨✨🌹🌹🌹✨✨✨✨✨
✨✨✨✨✨✨🌹✨✨✨✨✨✨""")
  time.sleep(0.2)
  await event.edit("""✨✨✨😻😻✨✨✨😻😻✨✨✨
✨✨😻😻😻😻✨😻😻😻😻✨✨
✨😻😻😻😻😻😻😻😻😻😻😻✨
✨😻😻😻😻😻😻😻😻😻😻😻✨
✨😻😻😻😻😻😻😻😻😻😻😻✨
✨✨😻😻😻😻😻😻😻😻😻✨✨
✨✨✨😻😻😻😻😻😻😻✨✨✨
✨✨✨✨😻😻😻😻😻✨✨✨✨
✨✨✨✨✨😻😻😻✨✨✨✨✨
✨✨✨✨✨✨😻✨✨✨✨✨✨""")
  time.sleep(0.2)
  await event.edit("""😘😘😘💋💋😘😘😘💋💋😘😘😘
😘😘💋💋💋💋😘💋💋💋💋😘😘
😘💋💋💋💋💋💋💋💋💋💋💋😘
😘💋💋💋💋💋💋💋💋💋💋💋😘
😘💋💋💋💋💋💋💋💋💋💋💋😘
😘😘💋💋💋💋💋💋💋💋💋😘😘
😘😘😘💋💋💋💋💋💋💋😘😘😘
😘😘😘😘💋💋💋💋💋😘😘😘😘
😘😘😘😘😘💋💋💋😘😘😘😘😘
😘😘😘😘😘😘💋😘😘😘😘😘😘""")
  time.sleep(0.2)
  await event.edit("""🌹🌹🌹😻😻🌹🌹🌹😻😻🌹🌹🌹
🌹🌹😻😻😻😻🌹😻😻😻😻🌹🌹
🌹😻😻😻😻😻😻😻😻😻😻😻🌹
🌹😻😻😻😻😻😻😻😻😻😻😻🌹
🌹😻😻😻😻😻😻😻😻😻😻😻🌹
🌹🌹😻😻😻😻😻😻😻😻😻🌹🌹
🌹🌹🌹😻😻😻😻😻😻😻🌹🌹🌹
🌹🌹🌹🌹😻😻😻😻😻🌹🌹🌹🌹
🌹🌹🌹🌹🌹😻😻😻🌹🌹🌹🌹🌹
🌹🌹🌹🌹🌹🌹😻🌹🌹🌹🌹🌹🌹""")
  time.sleep(0.2)
  await event.edit("""😻😻😻💗💗😻😻😻💗💗😻😻😻
😻😻💗💗💗💗😻💗💗💗💗😻😻
😻💗💗💗💗💗💗💗💗💗💗💗😻
😻💗💗💗💗💗💗💗💗💗💗💗😻
😻💗💗💗💗💗💗💗💗💗💗💗😻
😻😻💗💗💗💗💗💗💗💗💗😻😻
😻😻😻💗💗💗💗💗💗💗😻😻😻
😻😻😻😻💗💗💗💗💗😻😻😻😻
😻😻😻😻😻💗💗💗😻😻😻😻😻
😻😻😻😻😻😻💗😻😻😻😻😻😻""")
  time.sleep(0.2)
  await event.edit("""💓💓💓😘😘💓💓💓😘😘💓💓💓
💓💓😘😘😘😘💓😘😘😘😘💓💓
💓😘😘😘😘😘😘😘😘😘😘😘💓
💓😘😘😘😘😘😘😘😘😘😘😘💓
💓😘😘😘😘😘😘😘😘😘😘😘💓
💓💓😘😘😘😘😘😘😘😘😘💓💓
💓💓💓😘😘😘😘😘😘😘💓💓💓
💓💓💓💓😘😘😘😘😘💓💓💓💓
💓💓💓💓💓😘😘😘💓💓💓💓💓
💓💓💓💓💓💓😘💓💓💓💓💓💓""")
  time.sleep(0.2)
  await event.edit("""😘😘😘💕💕😘😘😘💕💕😘😘😘
😘😘💕💕💕💕😘💕💕💕💕😘😘
😘💕💕💕💕💕💕💕💕💕💕💕😘
😘💕💕💕💕💕💕💕💕💕💕💕😘
😘💕💕💕💕💕💕💕💕💕💕💕😘
😘😘💕💕💕💕💕💕💕💕💕😘😘
😘😘😘💕💕💕💕💕💕💕😘😘😘
😘😘😘😘💕💕💕💕💕😘😘😘😘
😘😘😘😘😘💕💕💕😘😘😘😘😘
😘😘😘😘😘😘💕😘😘😘😘😘😘""")
  time.sleep(0.2)
  await event.edit ("""💕💕💕🤗🤗💕💕💕🤗🤗💕💕💕
💕💕🤗🤗🤗🤗💕🤗🤗🤗🤗💕💕
💕🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗💕
💕🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗💕
💕🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗💕
💕💕🤗🤗🤗🤗🤗🤗🤗🤗🤗💕💕
💕💕💕🤗🤗🤗🤗🤗🤗🤗💕💕💕
💕💕💕💕🤗🤗🤗🤗🤗💕💕💕💕
💕💕💕💕💕🤗🤗🤗💕💕💕💕💕
💕💕💕💕💕💕🤗💕💕💕💕💕💕""")
  time.sleep(0.2)
  await event.edit ("""💝💝💝💋💋💝💝💝💋💋💝💝💝
💝💝💋💋💋💋💝💋💋💋💋💝💝
💝💋💋💋💋💋💋💋💋💋💋💋💝
💝💋💋💋💋💋💋💋💋💋💋💋💝
💝💋💋💋💋💋💋💋💋💋💋💋💝
💝💝💋💋💋💋💋💋💋💋💋💝💝
💝💝💝💋💋💋💋💋💋💋💝💝💝
💝💝💝💝💋💋💋💋💋💝💝💝💝
💝💝💝💝💝💋💋💋💝💝💝💝💝
💝💝💝💝💝💝💋💝💝💝💝💝💝""")
  time.sleep(0.2)
  await event.edit ("""💖💖💖😇😇💖💖💖😇😇💖💖💖
💖💖😇😇😇😇💖😇😇😇😇💖💖
💖😇😇😇😇😇😇😇😇😇😇😇💖
💖😇😇😇😇😇😇😇😇😇😇😇💖
💖😇😇😇😇😇😇😇😇😇😇😇💖
💖💖😇😇😇😇😇😇😇😇😇💖💖
💖💖💖😇😇😇😇😇😇😇💖💖💖
💖💖💖💖😇😇😇😇😇💖💖💖💖
💖💖💖💖💖😇😇😇💖💖💖💖💖
💖💖💖💖💖💖😇💖💖💖💖💖💖""")
  time.sleep(0.2)
  await event.edit ("""😍😍😍💗💗😍😍😍💗💗😍😍😍
😍😍💗💗💗💗😍💗💗💗💗😍😍
😍💗💗💗💗💗💗💗💗💗💗💗😍
😍💗💗💗💗💗💗💗💗💗💗💗😍
😍💗💗💗💗💗💗💗💗💗💗💗😍
😍😍💗💗💗💗💗💗💗💗💗😍😍
😍😍😍💗💗💗💗💗💗💗😍😍😍
😍😍😍😍💗💗💗💗💗😍😍😍😍
😍😍😍😍😍💗💗💗😍😍😍😍😍
😍😍😍😍😍😍💗😍😍😍😍😍😍""")
  time.sleep(0.2)
  await event.edit ("""💞💞💞😻😻💞💞💞😻😻💞💞💞
💞💞😻😻😻😻💞😻😻😻😻💞💞
💞😻😻😻😻😻😻😻😻😻😻😻💞
💞😻😻😻😻😻😻😻😻😻😻😻💞
💞😻😻😻😻😻😻😻😻😻😻😻💞
💞💞😻😻😻😻😻😻😻😻😻💞💞
💞💞💞😻😻😻😻😻😻😻💞💞💞
💞💞💞💞😻😻😻😻😻💞💞💞💞
💞💞💞💞💞😻😻😻💞💞💞💞💞
💞💞💞💞💞💞😻💞💞💞💞💞💞""")
  time.sleep(0.2)
  await event.edit ("""😌😌😌💕💕😌😌😌💕💕😌😌😌
😌😌💕💕💕💕😌💕💕💕💕😌😌
😌💕💕💕💕💕💕💕💕💕💕💕😌
😌💕💕💕💕💕💕💕💕💕💕💕😌
😌💕💕💕💕💕💕💕💕💕💕💕😌
😌😌💕💕💕💕💕💕💕💕💕😌😌
😌😌😌💕💕💕💕💕💕💕😌😌😌
😌😌😌😌💕💕💕💕💕😌😌😌😌
😌😌😌😌😌💕💕💕😌😌😌😌😌
😌😌😌😌😌😌💕😌😌😌😌😌😌""")
  time.sleep(0.2)
  await event.edit ("""💖💖💖😘😘💖💖💖😘😘💖💖💖
💖💖😘😘😘😘💖😘😘😘😘💖💖
💖😘😘😘😘😘😘😘😘😘😘😘💖
💖😘😘😘😘😘😘😘😘😘😘😘💖
💖😘😘😘😘😘😘😘😘😘😘😘💖
💖💖😘😘😘😘😘😘😘😘😘💖💖
💖💖💖😘😘😘😘😘😘😘💖💖💖
💖💖💖💖😘😘😘😘😘💖💖💖💖
💖💖💖💖💖😘😘😘💖💖💖💖💖
💖💖💖💖💖💖😘💖💖💖💖💖💖""")
  time.sleep(0.2)
  await event.edit ("""😇😇😇💗💗😇😇😇💗💗😇😇😇
😇😇💗💗💗💗😇💗💗💗💗😇😇
😇💗💗💗💗💗💗💗💗💗💗💗😇
😇💗💗💗💗💗💗💗💗💗💗💗😇
😇💗💗💗💗💗💗💗💗💗💗💗😇
😇😇💗💗💗💗💗💗💗💗💗😇😇
😇😇😇💗💗💗💗💗💗💗😇😇😇
😇😇😇😇💗💗💗💗💗😇😇😇😇
😇😇😇😇😇💗💗💗😇😇😇😇😇
😇😇😇😇😇😇💗😇😇😇😇😇😇""")
  time.sleep(0.2)
  await event.edit ("""💋💋💋😻😻💋💋💋😻😻💋💋💋
💋💋😻😻😻😻💋😻😻😻😻💋💋
💋😻😻😻😻😻😻😻😻😻😻😻💋
💋😻😻😻😻😻😻😻😻😻😻😻💋
💋😻😻😻😻😻😻😻😻😻😻😻💋
💋💋😻😻😻😻😻😻😻😻😻💋💋
💋💋💋😻😻😻😻😻😻😻💋💋💋
💋💋💋💋😻😻😻😻😻💋💋💋💋
💋💋💋💋💋😻😻😻💋💋💋💋💋
💋💋💋💋💋💋😻💋💋💋💋💋💋""")
  time.sleep(0.2)
  await event.edit(konec)
print(Fore.RED+"По всім питанням t.me://Satana_N666 \n ")
client.send_message('me', 'START')
print(Fore.GREEN + "   START ")
while z==1:
  for m in client.iter_messages('me', 1):
    if m.message == "exit":
      client.send_message('me', "ok")
      z=z+1
    elif m.message == "Exit" :
       client.send_message('me', "ok")
       z=z+1
