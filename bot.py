from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext

TOKEN = '7078975365:AAGyaxbZ74ozc1PLQy9tRQNG-vtfZuN2brM'
PHOTO_URL = 'https://github.com/hedred-z/telegram/blob/main/O-O.jpg?raw=true'
CHANNEL_URL = 'https://t.me/VortixCrypto'
WEB_APP_URL = 'https://hedred-z.github.io/Vetrix/'

async def start(update: Update, context: CallbackContext):
    caption = (
        "Welcome to Vortix🌪️\n\n"
        "At Vortix, we’re revolutionizing gaming with an exciting new experience in Telegram. "
        "Dive into our world where you can:\n\n"
        "💸 Play and Win: Engage in thrilling games and challenges to earn exclusive rewards.\n"
        "👥 Invite Friends: Bring your friends and family to join the fun. More friends mean more rewards!\n"
        "🎮 Complete Quests: Take on various quests and missions to rack up amazing bonuses!\n\n"
        "Get started now and see what incredible rewards await you! 💰\n\n"
        "Stay tuned and keep exploring! ⚡"
    )

    keyboard = [
        [InlineKeyboardButton("Launch Vortix 🌪️", web_app=dict(url=WEB_APP_URL))],
        [InlineKeyboardButton("Join Channel", url=CHANNEL_URL)]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_photo(
        photo=PHOTO_URL,
        caption=caption,
        reply_markup=reply_markup
    )

def main():
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler('start', start))

    application.run_polling()

if __name__ == '__main__':
    main()
