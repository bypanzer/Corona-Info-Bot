# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

import os
import requests
from requests.utils import requote_uri
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

FayasNoushad = Client(
    "Corona-Info-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

API = "https://api.sumanjay.cf/covid/?country="

START_TEXT = """
Salam {},Mən istənilən ölkənin koronavirus statistikasını verə biləcək sadə telegram botuyam.

"""
HELP_TEXT = """
Bu addımları izlə..
☛ İndi mənə istədiyin ölkə adını göndər...
☛ Mən məlumat toplayıb sənə göndərəcəm🙆.
"""

BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(Sahibim👽, url='https://telegram.me/sammekkim')
        ],[
        InlineKeyboardButton('⚙ Yeniliklər kanalı ⚙', url='https://telegram.me/EpicProjects')
        ]]
    )

@FayasNoushad.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.mention)
    reply_markup = BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup,
        quote=True
    )

@FayasNoushad.on_message(filters.private & filters.text)
async def reply_info(bot, update):
    reply_markup = BUTTONS
    await update.reply_text(
        text=covid_info(update.text),
        disable_web_page_preview=True,
        quote=True,
        reply_markup=reply_markup
    )

def covid_info(country_name):
    try:
        r = requests.get(API + requote_uri(country_name.lower()))
        info = r.json()
        country = info['country'].capitalize()
        active = info['active']
        confirmed = info['confirmed']
        deaths = info['deaths']
        info_id = info['id']
        last_update = info['last_update']
        latitude = info['latitude']
        longitude = info['longitude']
        recovered = info['recovered']
        covid_info = f"""
--**Covid 19 İnformasiyası**--

Ölkə : `{country}`
Aktiv xəstə sayı : `{active}`
Təsdiq edilmiş : `{confirmed}`
Ölüm sayı : `{deaths}`
ID : `{info_id}`
Ən son yenilənmə : `{last_update}`
En : `{latitude}`
Uzunluq : `{longitude}`
Sağalanlar : `{recovered}`

@EpicProjects tərəfindən hazırlandı.
"""
        return covid_info
    except Exception as error:
        return error

FayasNoushad.run()
