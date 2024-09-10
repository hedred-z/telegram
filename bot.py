from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler
from telegram.constants import ParseMode

TOKEN = '7078975365:AAGyaxbZ74ozc1PLQy9tRQNG-vtfZuN2brM'

async def start(update: Update, context):
    chat_id = update.message.chat_id
    image_url = 'https://example.com/image.jpg'
    welcome_text = (
        "Welcome to Vortix🌪️\n\n"
        "At Vortix, we’re revolutionizing gaming with an exciting new experience in Telegram. "
        "Dive into our world where you can:\n\n"
        "💸 **Play and Win**: Engage in thrilling games and challenges to earn exclusive rewards.\n"
        "👥 **Invite Friends**: Bring your friends and family to join the fun. More friends mean more rewards!\n"
        "🎮 **Complete Quests**: Take on various quests and missions to rack up amazing bonuses!\n\n"
        "Get started now and see what incredible rewards await you! 💰\n\n"
        "Stay tuned and keep exploring! ⚡"
    )
    keyboard = [
        [InlineKeyboardButton("Launch Vortix🌪️", url='https://example.com/launch')],
        [InlineKeyboardButton("Join our Channel", url='https://t.me/VortixCrypto')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_photo(
        chat_id=chat_id,
        photo=image_url,
        caption=welcome_text,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=reply_markup
    )

async def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    await application.start()
    await application.idle()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
