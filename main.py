import key as keys
from telegram.ext import *
import paswordgen as pas
import time as t

print("Bot started...")
def start_command(update,context):
    update.message.reply_text("Welcome to Password generator bot!!!!!")
    t.sleep(1)
    update.message.reply_text(
    """
/generate--> To generate a password
/Start-->To start the bot
/about-->To know about the bot
    """ )
    
def reply_message(update,context):
    update.message.reply_text("""
Enter the text in the format:
account_name,password_length
""")
    t.sleep(0.6)
    update.message.reply_text("""
for example:
xyz@gmail.com,10
    """)

def handle_message(update,context):
    stringcommand=(update.message.text)
    t=stringcommand.split(",")
    try:
        text=t[0]
        password=int(t[1])
    except:
        update.message.reply_text(
    """
    wrong format!!!!
    Enter in format:
    """)
        update.message.reply_text("""account,password_length""")
    password_gen=pas.random_generator(text,password)
    update.message.reply_text(password_gen)

def about_message(update,context):
    update.message.reply_text("""
This bot generates the 
password for your account 
according to the length you require...
press
/start-->start the bot   
    """)

def error(update,context):
    print(f"update{update} caused error{context.error}")

def main():
    updater=Updater(keys.API_KEY,use_context=True)
    dp=updater.dispatcher

    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("restart",start_command))
    dp.add_handler(CommandHandler("about",about_message))
    dp.add_handler(CommandHandler("generate",reply_message))
    dp.add_handler(MessageHandler(Filters.text,handle_message))
    dp.add_error_handler(error)


    updater.start_polling(3)
    updater.idle()

main()