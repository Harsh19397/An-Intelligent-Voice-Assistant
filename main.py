#We will call all the main functions here
#Importing libraries
from google_apis_speech_text_conversion import SpeechToText as stt
from google_apis_speech_text_conversion import TextToSpeech as tts
from Intent_detection import intentDetector as intent
import startup
from set_your_voice import set_your_audio
from Deep_Speaker.Activate_assistant import hot_word_activation
from functionalities import datetime, get_location, weatherInfor, google_search, youtube_search
import os

#Person using the assistant.
#Later fetch from the Database
User_name = "Harsh_Parashar"
#Triggered with a hot word
#Naming the assistant
assistant_name = "Gideon"

#Fetch from the DB later
#voice_set = False 
if not os.path.isfile("Recorded_Harsh_Parashar1.wav"):
    set_your_audio(User_name, assistant_name)

#Setting the hot word
#Later on fetch from the database
#hot_word = ""
#hot_word = startup.setting_up_hot_word(hot_word)
    
#Activate Assistant
activate = hot_word_activation(User_name, assistant_name)
if activate:
    tts.speak("Hello {}, You have activated me! Tell me how can I help you.".format(User_name))
    print("{}: Hello {}, You have activated me! Tell me how can I help you.".format(assistant_name, User_name))
else:
    tts.speak("Voice not matched! Try again later")
    print("Voice not matched! Try again later")
    
if activate:
    #Booting up the assistant with the startup messages and key fucnctionalities
    startup.startup_message()
    #Detect Intent and integrated with the funnctionality files
    
    while True:
        
        query = stt.speechToText().lower()
        intent_detected = intent.get_intent(query)
    
        if 'bye' or 'exit' in query:
            tts.speak("{}: Byee Sir!".format(assistant_name))
            print("{}: Byee Sir!".format(assistant_name))
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
    tts.speak("I dont listen to you! You are not privalleged enough to use my services.")
    print("{}: I dont listen to you! You are not privalleged enough to use my services.".format(assistant_name))        
