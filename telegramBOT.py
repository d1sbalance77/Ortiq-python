
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '6527631360:AAFM0E9wzrwzinBm5abD-fC0n2RDHwsedIg'
BOT_USERNAME: Final = '@Glass_Almaz1_bot'

async def start_command(upadete: Update, conteext: ContextTypes.DEFAULT_TYPE):
    await upadete.message.reply_text('Добро пожаловать! ')

async def start_command(upadete: Update, conteext: ContextTypes.DEFAULT_TYPE):
    await upadete.message.reply_text('Здесь вы можете узнать геолокацию нашего магазина и цены на продукт!')

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'Hello' in processed:
        return 'Hi'

async def handle_massage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Начинается...')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))


    app.add_handler(MessageHandler(filters.TEXT, handle_massage))

    app.add_error_handler(error)

    print('Работает...')
    app.run_polling(poll_interval=3)
