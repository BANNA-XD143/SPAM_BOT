from Aaru import BOT0,SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from Aaru import CMD_HNDLR as hl
    
HELP_PIC = "https://telegra.ph//file/2c892083ee3cd59674c31.jpg"

AARU_Help = "π₯ Aα΄Κα΄ Sα΄α΄α΄ Bα΄α΄ π₯\n\n"
 
AARU_Help += f"_α΄α΄Ι΄α΄s α΄α΄ α΄ΙͺΚα΄ΚΚα΄ ΙͺΙ΄ α΄α΄Κα΄ Κα΄α΄__\n\n"

AARU_Help += f" β§ πππ΄ππ±πΎπ π²πΌπ³π β§\n\n"

AARU_Help += f" `.ping` - to check ping\n `.alive` - to check bot alive/version (only main userbot will reply)\n .`restart` - to restart all spam bots \n `.addecho` - to addecho \n `.rmecho` - To remove Echo \n `.addsudo` - To add sudo user using spam bot \n\n"
 
AARU_Help += f" β§ π»π΄π°ππ΄ π²πΌπ³ β§\n\n"

AARU_Help += f" `.leave` - to leave public/private channel/groups\n\n"
 
AARU_Help += f" β§ ππΏπ°πΌ π²πΌπ³π β§\n\n"

AARU_Help += f" `.raid` - to raid\n `.replyraid` - to active reply raid\n `.dreplyraid` - to de-active reply raid\n `.spam` - this cmd use for Normal spam\n `.bigspam` - this cmd use for big spam\n `.uspam` - this cmd use for unlimited Spam until You restart the bots!!\n `.delayspam` - this cmd use for delay spam\n\n"

AARU_Help += f" .hotspam - Ιͺ α΄‘ΙͺΚΚ κ±α΄Ι’Ι’α΄κ±α΄ α΄α΄Ι΄'α΄ α΄κ±α΄ α΄ΚΙͺκ± α΄α΄α΄α΄α΄Ι΄α΄π β§\n\n"

AARU_Help += f"Β© @Aaru_Help\n"


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):               
    if event.sender_id in SUDO_USERS:
      await BOT0.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=ZAID_Help,
                                  buttons=[
        [
        Button.url("α΄Κα΄Ι΄Ι΄α΄Κ", "https://t.me/ABOUT_BANNA_XD")
        ] 
        ]
        )                                                         
