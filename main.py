from flask import Flask
from threading import Thread
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# === Your Bot Info ===
TOKEN = '7814360257:AAHMmOA3CxF4TeW72Td2qpwwgGCJAzxScBQ'
SITE_LINK = 'https://instayoutubevideo56878434442.netlify.app/'

# === Flask Web Server ===
app_web = Flask('')

@app_web.route('/')
def home():
    return "Bot is alive ✅"

def run():
    app_web.run(host='0.0.0.0', port=8080)

def keep_alive():
    thread = Thread(target=run)
    thread.start()

# === Telegram Bot Handlers ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome! Send me any YouTube or Instagram video link and I’ll help you download it."
    )

async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    button = InlineKeyboardMarkup(
        [[InlineKeyboardButton("📥 Download Video", url=SITE_LINK)]]
    )
    await update.message.reply_text(
        "✅ Click the button below to download your video:",
        reply_markup=button
    )

# === Run Everything ===
keep_alive()

bot_app = ApplicationBuilder().token(TOKEN).build()
bot_app.add_handler(CommandHandler("start", start))
bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))

print("🤖 Bot is running with Flask keep-alive...")
bot_app.run_polling()
