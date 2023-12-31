import pyshorteners , random , validators
from time import time , ctime
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
updater = Updater("ENV.API_KEY",
				use_context=True)


loaders = [ 'https://media.tenor.com/PlT4DtiUuvYAAAAM/i-get-the-job-done-cat.gif' , 'https://64.media.tumblr.com/f678ce38eb896bc1d4aaa911958af087/tumblr_n2eccv6Dev1rgpzseo1_1280.gif' , 'https://i.pinimg.com/originals/bf/34/61/bf34611d89cb4e9e62fc4997a1d329f2.gif' , 'https://miro.medium.com/max/720/1*3zTTejN8RKtodF2pkycGow.gif' , 'https://miro.medium.com/max/720/1*kWggO1y6n1sdfGpxZaAAGA.gif', 'https://images.squarespace-cdn.com/content/v1/54e2089fe4b0cc0f0867f658/1427813547778-UMUV7CWR2XT7D0HVQG5R/BikerBot.gif' , 'https://cdn.dribbble.com/users/1129235/screenshots/3017888/robo-1_1.gif' , 'https://i.pinimg.com/originals/b0/05/10/b0051024e16fb23cefe70c8499e76664.gif' , 'https://bugfender.com/wp-content/uploads/2018/10/automated.gif']


def start(update: Update, context: CallbackContext):
    name = str(update.message.from_user["first_name"])
    # ---logging---
    print(update.message.from_user.username , update.message.chat.first_name , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat.first_name) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    #  ---logging ends---
    update.message.reply_text(f"Hello {name}! You Can Send Me any url And I will shorten it Or Even Expand it if it is already Shortened!")


def send(update: Update, context: CallbackContext):
    user_link = str(update.message.text)
    # ---logging---
    print(update.message.from_user.username , update.message.chat.first_name , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat.first_name) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    #  ---logging ends---
    loading = update.message.reply_animation(animation = str(random.choice(loaders)) , caption = str(f"Converting Url: {user_link}"))
    is_valid = validators.url(user_link)

    if is_valid == True:
        compute = deal(user_link)
        if not compute == False:
            try:
                update.message.reply_text(str(f" Your New Url Is Here: `{compute}` ,\n ↑ Click To Copy ↑ "), disable_web_page_preview=True, parse_mode='MarkdownV2')
                context.bot.delete_message(message_id = loading.message_id , chat_id = update.message.chat_id)

            except Exception as Error_in_send:
                print(f"Error in send: {Error_in_send}")
                update.message.reply_text((f"Error in sending: {Error_in_send}"))
                context.bot.delete_message(message_id = loading.message_id , chat_id = update.message.chat_id)

        else:
            update.message.reply_text("Compute returned False! There is an error, Please Report To Developer @arhamSayyed ")
            print("Compute returned False")
            context.bot.delete_message(message_id = loading.message_id , chat_id = update.message.chat_id)
    else:
        update.message.reply_html(str(f""" The Url You provided: {user_link} is not a Valid Url! Please Check Format:
        
'google' --> Malformed
'google.com' --> Malformed
'http://google' --> Malformed
<b>'http://google.com' --> Valid </b>

 """), disable_web_page_preview=True)
        context.bot.delete_message(message_id = loading.message_id , chat_id = update.message.chat_id)

    



def help(update: Update, context: CallbackContext):
    update.message.reply_text("""
    
Format:        
'google' --> Malformed
'google.com' --> Malformed
'http://google' --> Malformed
'http://google.com' --> Valid""")
    # ---logging---
    print(update.message.from_user.username , update.message.chat.first_name , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat.first_name) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    #  ---logging ends---






def deal(link):

    try:

        shortener = pyshorteners.Shortener()
        shortened_URL = shortener.tinyurl.short(link)
        return shortened_URL
    except Exception as error:
        print(f"Error in deal --> shortening: {error}")

        try:
            shortener = pyshorteners.Shortener()
            expanded_URL = shortener.tinyurl.expand(link)
            return expanded_URL
        except Exception as error:
            print(f"Error in deal --> expanding: {error}")




def donate(update: Update, context: CallbackContext):
    update.message.reply_html(
str(f"""
<b> Thanks A lot {update.message.chat.first_name} For Even Thinking Of Donating! </b>
"""))
    update.message.reply_photo ( photo="https://i.postimg.cc/s2L6tny7/share-image7285879562483283294.png" , caption="You Can Send Money On This QR Or If You Want Send it to This UPI ID: `arhamsayyed.famc@idfcbank` " , parse_mode='MarkdownV2')
    # ---logging---
    print(update.message.from_user.username , update.message.chat.first_name , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat.first_name) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    #  ---logging ends---




def contact(update: Update, context: CallbackContext):
    update.message.reply_html(
str(f"""
Hello {update.message.chat.first_name},
I am <b> @ArhamSayyed </b>
I am an enthusiast in <a href='https://en.wikipedia.org/wiki/Python_(programming_language)'> python programming </a> &  <a href='https://www.opc-router.com/what-is-a-telegram-bot/'> telegram bot </a> development 
I am a Student, Ready to <a href = 'https://t.me/Arhamsayyed'> Freelance </a>
And if you Want you can \n /BuyCoffee for me

""") ,

 disable_web_page_preview=True)
     # ---logging---
    print(update.message.from_user.username , update.message.chat.first_name , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat.first_name) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    #  ---logging ends---








updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('BuyCoffee', donate))
updater.dispatcher.add_handler(CommandHandler('contact', contact))
updater.dispatcher.add_handler(CommandHandler('help', help))


updater.dispatcher.add_handler(MessageHandler(Filters.text, send))


updater.start_polling()
print("polling started...")
