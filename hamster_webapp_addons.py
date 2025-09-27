
# -*- coding: utf-8 -*-
"""
Hamster WebApp qo‘shimchalari (python-telegram-bot v20+)
- /app — WebApp tugmasi (KeyboardButton bilan)
- WEB_APP_DATA qabul qilish va bot ichida ishlov berish
*** Muhim: sendData faqat KeyboardButton orqali ochilgan WebApp bilan ishlaydi (inline emas). ***
"""

import json
from telegram import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from telegram.ext import MessageHandler, filters

# 1) /app komandasi: WebApp ochuvchi tugma yuboramiz
async def app_cmd(update, context):
    webapp_url = "https://<sizning-hosting-url>/index.html"  # GitHub Pages/Netlify URL’ingiz
    kb = ReplyKeyboardMarkup.from_button(
        KeyboardButton(text="🔗 Open Hamster App", web_app=WebAppInfo(url=webapp_url))
    , resize_keyboard=True, one_time_keyboard=True)
    await update.message.reply_text("Mini App’ni ochish uchun tugmani bosing:", reply_markup=kb)

# 2) WebApp’dan kelgan ma’lumotlarni ushlash
async def handle_webapp_data(update, context):
    try:
        wad = update.message.web_app_data  # telegram.WebAppData
        data = json.loads(wad.data) if wad and wad.data else {}
    except Exception:
        data = {}

    action = data.get("action")
    user = update.effective_user

    # mavjud bot logikalaringizga ulang:
    if action == "tap":
        # shu yerda 'tap' bilan bir xil ichki funksiyangizni chaqiring
        await update.message.reply_text("🐹 TAP qabul qilindi! (WebApp)")
    elif action == "daily":
        await update.message.reply_text("🎁 DAILY so‘rovi qabul qilindi! (WebApp)")
    elif action == "stats":
        await update.message.reply_text("📊 STATS so‘rovi qabul qilindi! (WebApp)")
    else:
        await update.message.reply_text("Nomaʼlum amaliyot.")

def add_webapp_handlers(app):
    # app.add_handler(CommandHandler("app", app_cmd))  # asosiy faylda qo‘shasiz
    app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_webapp_data))
