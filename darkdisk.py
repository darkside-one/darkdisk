import telebot
import yadisk
import tempfile

yd = yadisk.YaDisk(token='YOUR_YANDEX_DISK_TOKEN')
bot = telebot.TeleBot('YOUR_BOT_TOKEN')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Please send a file to download to Yandex disk")

@bot.message_handler(content_types=['document'])
def handle_docs(message):
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with tempfile.NamedTemporaryFile(delete=False, mode='wb') as f:
        f.write(downloaded_file)
        yd.upload(f.name, message.document.file_name)
    bot.reply_to(message, "File has been saved to Yandex Disk!")

bot.polling()