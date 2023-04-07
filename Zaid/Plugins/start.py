from Zaid import Zaid
from telethon import events, Button
import random
from .language import translate
import re
from telethon.tl.types import Message
from telethon.tl.custom import Button
from telethon.events import NewMessage, CallbackQuery
import asyncio
from telethon.errors.rpcerrorlist import (
    FloodWaitError,
    UserBlockedError,
    ChatWriteForbiddenError,
)
from .. import CMD_HELP
from google_trans_new.constant import LANGUAGES
from google_trans_new import google_translator
translator = google_translator()
from Zaid.utils import Zbot, Zinline
from Zaid.Plugins.sql.language import set_lang as set_langu

IMG = ["https://te.legra.ph/file/ff591945eae13d0454e13.jpg",
       "https://te.legra.ph/file/ff591945eae13d0454e13.jpg",
       "https://te.legra.ph/file/ff591945eae13d0454e13.jpg",
       "https://te.legra.ph/file/5d8d6445636005a6d1468.jpg",
       "https://te.legra.ph/file/5d8d6445636005a6d1468.jpg"
]
line = "───────────────────────"

plugins = [
    "⛑️ 𝐚𝐝𝐦𝐢𝐧 🎩",
    "🤖 𝐀𝐅𝐊 🆘",
    "𝐀𝐏𝐑𝐎𝐕𝐄𝐋",
    "𝐂𝐇𝐀𝐓-𝐁𝐎𝐓",
    "𝐅𝐈𝐋𝐓𝐄𝐑𝐒",
    "𝐆𝐑𝐄𝐄𝐓𝐈𝐍𝐆𝐒",
    "𝐋𝐎𝐂𝐊𝐒",
    "𝐒𝐓𝐈𝐂𝐊𝐄𝐑",
    "𝐑𝐔𝐋𝐄𝐒",
    "𝐒𝐎𝐍𝐆𝐒",
    "𝐑𝐄𝐏𝐎𝐑𝐓𝐒",
    "𝐐𝐔𝐎𝐓𝐋𝐘",
    "𝐏𝐔𝐑𝐆𝐄𝐒",
    "𝐏𝐈𝐍𝐒",
    "𝐌𝐈𝐂𝐒",
    "𝐅𝐎𝐑𝐂𝐄-𝐒𝐔𝐁",
    "𝐄𝐗𝐓𝐑𝐀𝐒",
    "𝐁𝐀𝐍𝐒",
    "𝐁𝐋𝐎𝐂𝐊𝐋𝐈𝐒𝐓",
    "𝐀𝐍𝐓𝐈𝐅𝐋𝐎𝐎𝐃",
    "𝐂𝐀𝐏𝐓𝐂𝐇𝐀",
    "𝐖𝐀𝐑𝐍𝐈𝐍𝐆𝐒",
]

@Zbot(pattern="^/start ?(.*)")
async def start(event):
    hi = translate("Hello", event.chat_id)
    if event.is_private:
       IMSG = f"{random.choice(IMG)}"
       # remove # to enable translater in pm
       #hj = translate("✘ I am an group management bot with some fun extra ;)", event.chat_id)
       #hj2 = translate("✘ I can do a Verity of things, most common of em are:", event.chat_id)
       #hj3 = translate("‣ Restrict users with ban permission.", event.chat_id)
       #hj4 = translate("‣ Greet users with media + text and buttons, with proper formatting.", event.chat_id)
       #hj5 = translate("‣ Warn users according to the options set and restrict them accordingly.", event.chat_id)
       #hj6 = translate("‣ Save notes and filters with proper formatting and reply markup.", event.chat_id)
       #hj7 = translate("‣ I can play music in your groups voice chat", event.chat_id)
       #hj8 = translate("‣ I have many features which you like", event.chat_id)
       #hj9 = translate("to change the bot language", event.chat_id)
       #hj10 = translate("There's even more! This is just the tip of the iceberg. Do note i need to be promoted with proper admin permission to perform from. else won't be able to perform as said.", event.chat_id)
       hj = "✘ I am an group management bot with some fun extra ;)"
       hj2 = "✘ I can do a Verity of things, most common of em are:"
       hj3 = "‣ Restrict users with ban permission."
       hj4 = "‣ Greet users with media + text and buttons, with proper formatting."
       hj5 = "‣ Warn users according to the options set and restrict them accordingly."
       hj6 = "‣ Save notes and filters with proper formatting and reply markup."
       hj7 = "‣ I can play music in your groups voice chat"
       hj8 = "‣ I have many features which you like"
       hj9 = "to change the bot language"
       hj10 = "There's even more! This is just the tip of the iceberg. Do note i need to be promoted with proper admin permission to perform from. else won't be able to perform as said."
       await event.reply(
             f"{hi} {event.sender.first_name}\n{line}\n{hj}\n{hj2}\n{hj3}\n{hj4}\n{hj5}\n{hj6}\n{hj7}\n{hj8}\n‣ /setlang {hj9}\n{line}\n{hj10}", 
             buttons=[
        [Button.url("𝐚𝐝𝐝 𝐦𝐞 𝐦𝐨𝐢 𝐥𝐮𝐛 ➕", url="t.me/Zaid2_Robot?startgroup=true")],
        [Button.url("𝐩𝐡𝐲𝐬𝐜𝐨-𝐡𝐞𝐥𝐩 📢", url="t.me/music_bot122"), Button.url("𝐏𝐡𝐲𝐬𝐜𝐨-𝐡𝐞𝐥𝐩", url="t.me/music_bot122")],
        [Button.inline("𝐥𝐚𝐧𝐠𝐮𝐠𝐞 🌐", data=f"langs"), Button.inline("𝐇𝐞𝐥𝐩 ⁉️", data="help_menu")]])
    if event.is_group:
        IMSG = f"{random.choice(IMG)}"
        await event.client.send_file(event.chat_id,
             IMSG,
             caption="{} {}".format(hi, event.sender.first_name), 
             buttons=[
         [Button.url("𝐀𝐝𝐝 𝐦𝐨𝐢 𝐥𝐮𝐛  ➕", url="t.me/sunitarobot?startgroup=true")]])


JSONDB = None

if not JSONDB:
    JSONDB = {"users": [], "language": {}}


def split_list(lis, index):
    new_ = []
    while lis:
        new_.append(lis[:index])
        lis = lis[index:]
    return new_


Buttons = [Button.inline(LANGUAGES[lang].upper(), f"stt-{lang}") for lang in LANGUAGES]
# 2 Rows
Buttons = split_list(Buttons, 2)
# 5 Columns
Buttons = split_list(Buttons, 5)





@Zinline(pattern=r"langs")
async def set_language(event):
    if not event.is_private:
       try:
           _s = await event.client.get_permissions(event.chat_id, event.sender_id)
           if not _s.is_admin:
              return
       except Exception:
           pass
    bts = Buttons[0].copy()
    bts.append([Button.inline("𝐍𝐞𝐱𝐭 ▶", "btshh"), Button.inline("𝐜𝐚𝐧𝐜𝐞𝐥 ❌", "cncll")])
    await event.edit("Choose your desired language..", buttons=bts)


@Zinline(pattern=r"btshh(.*)")
async def click_next(event):
    if not event.is_private:
       try:
           _s = await event.client.get_permissions(event.chat_id, event.sender_id)
           if not _s.is_admin:
              return
       except Exception:
           pass
    data = event.data_match.group(1).decode("utf-8")
    if not data:
        val = 1
    else:
        prev_or_next = data[0]
        val = int(data[1:])
        if prev_or_next == "p":
            val -= 1
        else:
            val += 1
    try:
        bt = Buttons[val].copy()
    except IndexError:
        val = 0
        bt = Buttons[0].copy()
    if val == 0:
        bt.append([Button.inline("𝐍𝐞𝐱𝐭 ▶", "btshh"), Button.inline("Cancel ❌", "cncll")])
    else:
        bt.extend(
            [
                [
                    Button.inline("◀ 𝐏𝐫𝐞𝐯", f"btshhp{val}"),
                    Button.inline("𝐍𝐞𝐱𝐭 ▶", f"btshhn{val}"),
                ],
                [Button.inline("🚫 𝐂𝐚𝐧𝐜𝐞𝐥 ☢️", "cncll")],
            ]
        )
    await event.edit(buttons=bt)


@Zinline(pattern=r"cncll")
async def maggie(event):
    if not event.is_private:
       try:
           _s = await event.client.get_permissions(event.chat_id, event.sender_id)
           if not _s.is_admin:
              return
       except Exception:
           pass
    await event.delete()



@Zinline(pattern=r"stt-(.*)")
async def set_lang(event):
    match = event.data_match.group(1).decode("utf-8")
    if not event.is_private:
       try:
           _s = await event.client.get_permissions(event.chat_id, event.sender_id)
           if not _s.is_admin:
              return
       except Exception:
           pass
    set_langu(event.chat_id, match)
    code_lang = {code: name for code, name in LANGUAGES.items()}
    name = code_lang[match]
    name = name[0].upper() + name[1:]
    await event.edit(f"Language successfully changed to {name} !")



@Zbot(pattern="^/help ?(.*)")
async def help(event):
    if event.is_group:
        buttons = [
            [Button.url("❔ 𝐡𝐞𝐥𝐩", "https://t.me/sunitarobot?start=_help")],
        ]
        await event.reply(
            "Contact me in PM to get the list of possible commands.",
            buttons=buttons,
        )
    elif event.is_private:
        buttons = paginate_help()
        await event.reply("Here You can Find all Commands", buttons=buttons)


@Zinline(pattern=r"us_plugin_(.*)")
async def us_0(event):
    pl_name = (event.pattern_match.group(1)).decode()
    try:
        pl_help = CMD_HELP[pl_name][1]
    except KeyError:
        pl_help = "The help menu for this module will be provided soon!"
    await event.edit(
        pl_help,
        buttons=[
            Button.inline("Close", data="cncll"),
            Button.inline("Back", data="help_menu"),
        ],
    )

@Zinline(pattern=r"help_menu")
async def help_menu(event):
    buttons = paginate_help()
    await event.edit("Here You can Find all Commands", buttons=buttons)

@Zbot(pattern="^/start _help")
async def st_help(e):
    buttons = paginate_help()
    await e.respond("Here You can Find all Commands", buttons=buttons)


def paginate_help():
    helpable_plugins = sorted(plugins)
    modules = [
        Button.inline(x, data=f"us_plugin_{x.lower()}") for x in helpable_plugins
    ]
    pairs = list(
        zip(
            modules[::3],
            modules[1::3],
            modules[2::3],
        )
    )
    modulo_page = 0 % 1
    pairs = pairs[modulo_page * 8 : 8 * (modulo_page + 1)] + [
        (Button.inline("Close", data="cncll"),)
    ]
    return pairs
