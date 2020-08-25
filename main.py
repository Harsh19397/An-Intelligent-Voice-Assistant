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
from functionalities import google_search, youtube_search
import os, json

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
            elif intent_detected == 'intent.google_search':
                print("You: {}".format(query))
                google_search.google_search(query)
            elif intent_detected == 'intent.youtube':
                print("You: {}".format(query))
                youtube_search.youtube_search(query)
            elif intent_detected == 'intent.text_message':
                print("You: {}".format(query))
                pass
            elif intent_detected == 'intent.brightness_control':
                print("You: {}".format(query))
                pass
            elif intent_detected == 'intent.route_information':
                print("You: {}".format(query))
                pass
            elif intent_detected == 'intent.calender':
                print("You: {}".format(query))
                pass
            elif intent_detected == 'intent.contact':
                print("You: {}".format(query))
                pass
            elif intent_detected == 'intent.notifications':
                print("You: {}".format(query))
                pass
            elif intent_detected == 'intent.wallpaper':
                print("You: {}".format(query))
                pass
            elif intent_detected == 'intent.weather':
                print("You: {}".format(query))
                pass
            
            else:
                print("You: {}".format(query))
                tts.speak("{}: Couldn't understand you".format(assistant_name))
                print("{}: Couldn't understand you".format(assistant_name))

else:
    print("Your voice dosent match with the owner!")
    tts.speak("Your voice dosent match with the owner!")
