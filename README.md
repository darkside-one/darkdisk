# darkdisk
Telegram Bot, that receives a file and uploads it to Yandex Disk

This is a Telegram bot that utilizes the Telebot and Yandex Disk (yadisk) libraries in Python. When the user sends the '/start' command, the bot responds with instructions for the user to send a file for download. When the user sends a file, the bot uses the Telebot library to download the file, then it uses the yadisk library to upload the file to the user's Yandex Disk. The bot then sends a message confirming that the file has been saved to Yandex Disk.
