import pyshorteners , random 
from time import time , ctime
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
updater = Updater("5764653780:AAF4b-Mv6WY-dZsXRDfVPZ2ALouG0uMg_OY",
				use_context=True)


modules = ['chilpit' , 'tinyurl' , 'clckru' , 'dagd' , 'isgd']

welcome_animate = ['https://media.tenor.com/5hKPyupKGWMAAAAC/robot-hello.gif' , 'https://media.tenor.com/axrso9GQCKkAAAAC/robot-talk.gif' , 'https://media1.giphy.com/media/Nc2slkPLPdpmWeCUZc/giphy.gif?cid=ecf05e47de8ebqw9pl62zc3bwbsw7ik5kf814dy638fq6ux2&rid=giphy.gif&ct=g'] 
welcome_messages = ['Heyaaaa!!!! %s ' , "Hi! %s I am a Bot! I'll help you Deal with URLs " , 'I Welcomes %s' , 'Hi! %s' , 'Hello Mr/Ms %s']
loaders = [ 'https://media.tenor.com/PlT4DtiUuvYAAAAM/i-get-the-job-done-cat.gif' , 'https://64.media.tumblr.com/f678ce38eb896bc1d4aaa911958af087/tumblr_n2eccv6Dev1rgpzseo1_1280.gif' , 'https://i.pinimg.com/originals/bf/34/61/bf34611d89cb4e9e62fc4997a1d329f2.gif' , 'https://miro.medium.com/max/720/1*3zTTejN8RKtodF2pkycGow.gif' , 'https://miro.medium.com/max/720/1*kWggO1y6n1sdfGpxZaAAGA.gif', 'https://images.squarespace-cdn.com/content/v1/54e2089fe4b0cc0f0867f658/1427813547778-UMUV7CWR2XT7D0HVQG5R/BikerBot.gif' , 'https://cdn.dribbble.com/users/1129235/screenshots/3017888/robo-1_1.gif' , 'https://i.pinimg.com/originals/b0/05/10/b0051024e16fb23cefe70c8499e76664.gif' , 'https://bugfender.com/wp-content/uploads/2018/10/automated.gif']
loading_messeges = ['HangOn 🍻! Until I Deal with URL.... 😎' , 'Cutting URL!.... ' ,  'Collecting resources....' , 'Getting algorithm ready.... ' , 'Validating URL.... ' , 'Getting Server Ready....'] 
job_done_animate = [ 'https://media.tenor.com/CW3dv0a1Hf4AAAAM/mission-complete-spongebob.gif' ,  'https://c.tenor.com/OfvU2xH4EpkAAAAM/thumbs-up-good-job.gif' , 'https://media.tenor.com/IAUvvrUY7zQAAAAM/done-spongebob.gif' , 'https://monzo.com/static/images/blog/2017-09-29-android-engineers/dude.gif' , 'https://media3.giphy.com/media/dup8JTRGfu41esoibk/giphy.gif?cid=790b76117f502aae5b58cdae7c83f506a0a08b5c9c54b4a9&rid=giphy.gif&ct=g']  
errors_animate = [ 'https://media.tenor.com/qeS6BuiV_08AAAAM/baby-punch.gif' , 'https://media.tenor.com/ACy8YfHUofwAAAAM/fail-robot.gif' , 'https://media.tenor.com/z0rwZrP0ylwAAAAM/elize-ryd-amaranthe.gif' , 'https://media.tenor.com/OxvVRFnPZO8AAAAM/error-the-simpsons.gif' , 'https://media3.giphy.com/media/U8MnmuVDpK264/giphy.gif?cid=ecf05e47jbqxbkogaulkdfrmkp8b3l52q9yld9q5sprgs4ed&rid=giphy.gif&ct=g','https://media0.giphy.com/media/L4BK799epTvSsNXSjr/giphy.gif?cid=790b7611da0f184e9b4da0ef7a46414be3123d8fbd0fb131&rid=giphy.gif&ct=s' , 'https://media3.giphy.com/media/8L0Pky6C83SzkzU55a/giphy.gif?cid=790b76113c378884712a8d4baaeb747c7d2bbdff8ad8be8b&rid=giphy.gif&ct=g' , 'https://external-preview.redd.it/MNcyuoDrG3VvGINMxwbsNb7spDTtCcKkaRu4poc7fKI.gif?format=mp4&s=b450aa23274d29781538bf4faf2dd316734af32e'] 


shorting = """update.message.reply_text(str(shortener.%s.short(link))) """

# expanding = """update.message.reply_text(str(shortener.%s.expand(link))) """


def start(update: Update, context: CallbackContext):
	try:
		data = update.message.from_user
		user_name = data['username']
		if user_name == None:
			user_name = "You"
		else:
			pass
		update.message.reply_animation(animation = str(random.choice(welcome_animate)) , caption = (str(random.choice(welcome_messages)) %user_name))
		update.message.reply_text("You Can Just Send The Url You Wanna Shorten or Expand 😉")
		
	except Exception as error_message:
		print("You have to fix: %s in /start" %error_message)
		update.message.reply_animation(animation = random.choice(errors_animate) , caption = str("Oops! 🥴 An Error Occured: %s Please Do me a favour by reporting error to Developer @Arhamsayyed") %error_message )




def deal(update: Update, context: CallbackContext):
    if len(update.message.text)  < 4000:
        loading = update.message.reply_animation(animation = str(random.choice(loaders)) , caption = str(random.choice(loading_messeges)))
        try:
            shortener = pyshorteners.Shortener()
            link = str(update.message.text)
            exec(shorting %random.choice(modules))
            update.message.reply_animation( animation = str(random.choice(job_done_animate)) , caption = str("Done!"))
            context.bot.delete_message(message_id = loading.message_id , chat_id = update.message.chat_id)
            current_DateTime = time()
            print("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
        
        except:
            shortener = pyshorteners.Shortener()
            link = str(update.message.text)
            try:
                update.message.reply_text(shortener.chilpit.expand(link))
            except:
                try:
                    update.message.reply_text(shortener.tinyurl.expand(link))
                except:
                    try:
                        update.message.reply_text(shortener.clckru.expand(link))
                    except:
                        try:
                            update.message.reply_text(shortener.dagd.expand(link))
                        except:
                            update.message.reply_text(shortener.isgd.expand(link))
            update.message.reply_animation( animation = str(random.choice(job_done_animate)) , caption = str("Done!"))
            context.bot.delete_message(message_id = loading.message_id , chat_id = update.message.chat_id)
            current_DateTime = time()
            print("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))


    else:
        context.bot.delete_message(message_id = loading.message_id , chat_id = update.message.chat_id)
        update.message.reply_sticker("😬")
        update.message.reply_animation(animation = random.choice(errors_animate) , caption = str("Uhh ohh too long url! "))








updater.dispatcher.add_handler(CommandHandler('start', start))



updater.dispatcher.add_handler(MessageHandler(Filters.text, deal))


updater.start_polling()
print("polling started...")
