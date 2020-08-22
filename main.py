#We will call all the main functions here
#Importing libraries
import numpy as np
import pandas as pd
import speech_recognition as sr
from google_apis_speech_text_conversion import SpeechToText as stt
from google_apis_speech_text_conversion import TextToSpeech as tts
from functionalities import listen_audio as listen
import intentDetector as intent
import startup
from functionalities import datetime, get_location, weatherInfor, google_search, youtube_search

#Triggered with a hot word
#Naming the assistant

#Booting up the assistant with the startup messages and key fucnctionalities
startup.startup_message()
#Setting the hot word
#Later on fetch from the database
hot_word = ""
hot_word = startup.setting_up_hot_word(hot_word)

#Detect Intent and integrated with the funnctionality files

while True:
    
    query = stt.speechToText().lower()
    intent_detected = intent.get_intent(query)

    if 'bye' or 'exit' in query:
        tts.speak("Byee Sir!")
        break
    elif intent_detected == 'intent.google_search':
        google_search.google_search(query)
    elif intent_detected == 'intent.youtube':
        youtube_search.youtube_search(query)
    elif intent_detected == 'intent.text_message':
        pass
    elif intent_detected == 'intent.brightness_control':
        pass
    elif intent_detected == 'intent.route_information':
        pass
    elif intent_detected == 'intent.calender':
        pass
    elif intent_detected == 'intent.contact':
        pass
    elif intent_detected == 'intent.notifications':
        pass
    elif intent_detected == 'intent.wallpaper':
        pass
    elif intent_detected == 'intent.weather':
        pass
    
    else:
        tts.speak("Couldn't understand you")
        
