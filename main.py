#We will call all the main functions here
#Importing libraries
from google_apis_speech_text_conversion import SpeechToText as stt
from google_apis_speech_text_conversion import TextToSpeech as tts
from Intent_detection import intentDetector as intent
import startup
from Trigger_word_detection.detect_trigger import trigger_word_detection as trigger
from set_your_voice import set_your_audio
from Deep_Speaker.Activate_assistant import hot_word_activation
from Trigger_word_detection import detect_trigger
from functionalities import google_search, youtube_search, brightness, datetime, news_module
from functionalities import get_location, jokes, launching_applications,movies_on_streaming_platforms
from functionalities import play_music
import os, json
import webbrowser

#Loading startup functions during boot time
webbrowser.register('chrome',
                       None,
                       webbrowser.BackgroundBrowser("C:/Program Files (x86)/Google/Chrome/Application/chrome"))

#Person using the assistant.
#Signing up
#Connecting with a database stored locally
database = open('./Database/database.json')
db = json.load(database)
database.close()
#logging in
print("Assistant: Hey there! May I know who are you?")
tts.speak("Hey there! May I know who are you?")
User_name = stt.speechToText()

#Fetching Username from the database
try:
    User_Name = db[User_name]["User_name"]
except:
    print("I cannot find {} in the database! Would you like to register to use my services.".format(User_name))
    tts.speak("I cannot find {} in the database! Would you like to register to use my services.".format(User_name))
    res = stt.speechToText()
    if res.lower() == 'yes':
        print("What would you like to name me?")
        tts.speak("What would you like to name me?")
        ass_name = stt.speechToText()
        print("{}:{} ".format(User_name, ass_name))
        print("What will be your password?")
        tts.speak("What will be your password?")
        password_new = stt.speechToText()
        print("Thank you for saving your password!")
        tts.speak("Thank you for saving your password!")
        set_your_audio(User_name)
        j_obj = {User_name:{"User_name": User_name,
                 "Password": password_new,
                 "assistant_name": ass_name,
                 "voice set": True}}
        db.update(j_obj)
        database = open('./Database/database.json', 'w+')
        json.dump(db, database, indent = 4)
        database.close()

    else:
        tts.speak("Sorry! I cannot help you.")
        print("Sorry! I cannot help you.")

#Loading the database
database = open('./Database/database.json')
db = json.load(database)
User_Name = db[User_name]["User_name"]
database.close()


#Password for the active User
Password_for_active_user = db[User_Name]["Password"]

#Assistant Name
assistant_name = db[User_Name]["assistant_name"]

#Login Functionality
print("{}: Hello {}, In order to proceed further, you will have to speak out your password!".format(assistant_name, User_name))
tts.speak("Hello {}, In order to proceed further, you will have to speak out your password!".format(User_name))
pass_user = hot_word_activation(User_name, assistant_name)

#Add a functionality for changing
if pass_user:
    #Fetch from the DB later
    #voice_set = False
    tts.speak("Welcome {}!".format(User_Name))
    print("{}: Welcome {}!".format(assistant_name, User_Name))

    activate = trigger(Password_for_active_user)

    while activate:
        #Booting up the assistant with the startup messages and key fucnctionalities
        #Detect Intent and integrated with the funnctionality files

        while True:

            query = stt.speechToText().lower()
            intent_detected = intent.get_intent(query)

            if 'bye' or 'exit' or 'deactivate' in query:
                tts.speak("{}: Byee Sir!".format(assistant_name))
                print("{}: Byee Sir!".format(assistant_name))
                activate = False
                break

            #Google search
            elif intent_detected == 'intent.google_search':
                print("You: {}".format(query))
                google_search.google_search(query)

            #Youtube search
            elif intent_detected == 'intent.youtube':
                print("You: {}".format(query))
                youtube_search.youtube_search(query)

            #Brightness control
            elif intent_detected == 'intent.brightness':
                print("You: {}".format(query))
                brightness.brightness_control(assistant_name, query)

            #Datetime
            elif intent_detected == 'intent.datetime':
                print("You: {}".format(query))
                time, month = datetime.get_date_time()
                time = str(time).split('.')
                time = time[0].split()
                hour = time[1].split(':')[0]
                minutes = time[1].split(':')[1]
                day = time[0].split('-')[2]
                year = time[0].split('-')[0]
                print("{}: Its {} hours and {} minutes of {} {} {}".format(assistant_name, hour, minutes, day, month, year))
                tts.speak("Its {} hours and {} minutes of {} {} {}".format(hour, minutes, day, month, year))

            #Brightness control
            elif intent_detected == 'intent.brightness':
                print("You: {}".format(query))
                brightness.brightness_control(assistant_name, query)

            #Get_location
            elif intent_detected == 'intent.location':
                print("You: {}".format(query))
                location = get_location.get_current_location()
                print("{}: You are at {}.".format(assistant_name, location))
                tts.speak("You are at {}.".format(location))

            #Jokes
            elif intent_detected == 'intent.joke':
                print("You: {}".format(query))
                jokes.get_jokes(assistant_name)

            #Launch Application
            elif intent_detected == 'intent.launchApplication':
                print("You: {}".format(query))
                launching_applications.launch_application(assistant_name, query)

            #Stream_movies
            elif intent_detected == 'intent.streamMovie':
                print("You: {}".format(query))
                movies_on_streaming_platforms.stream_movie(assistant_name, query)

            #News
            elif intent_detected == 'intent.news':
                print("You: {}".format(query))
                news_module.get_news(assistant_name, query)

            #Play music
            elif intent_detected == 'intent.playMusic':
                print("You: {}".format(query))
                news_module.get_news(assistant_name, query)

            else:
                print("You: {}".format(query))
                tts.speak("{}: Couldn't understand you".format(assistant_name))
                print("{}: Couldn't understand you".format(assistant_name))

else:
    print("Your voice dosent match with the owner!")
    tts.speak("Your voice dosent match with the owner!")
