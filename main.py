#We will call all the main functions here
#Importing libraries
import numpy as np
import pandas as pd
import speech_recognition as sr
from Intent_detection import SpeechToText as stt
from Intent_detection import TextToSpeech as tts
from functionalities import listen_audio as listen
from functionalities import datetime, get_location, weatherInfor

#Triggered with a hot word

#Assitant Name
Assistant_name = ""
#Start_up
current_time, month = datetime.get_date_time()
current_temperature, current_pressure, current_humidiy, weather_description = weatherInfor.get_weather(get_location.get_current_location())

#Naming the assistant
if len(Assistant_name) == 0:
    print("Hello Sir! This is the first time that we have met. I am your Artificial Intelligence based assistant. What would you like to call me?")
    tts.speak("Hello Sir! This is the first time that we have met. I am your Artificial Intelligence based assistant. What would you like to call me?")
    Assistant_name = stt.speechToText()
    tts.speak("Thank you for naming me {} Sir! ".format(Assistant_name))
    
#Activation message    
if current_time.hour < 12:
    print("Hello Sir, A very good morning to you! It is {} hundred {} hours on {} of {} {} with {} degree celcius, {} percent humidity and {} here in {}"
          .format(current_time.hour, 
                  current_time.minute, 
                  current_time.day, month,  
                  current_time.year,
                  current_temperature,
                  current_humidiy,
                  weather_description,
                  get_location.get_current_location()))
    tts.speak("Hello Sir, A very good morning to you! It is {} hundred {} hours on {} of {} {} with {} degree celcius, {} percent humidity and {} here in {}"
          .format(current_time.hour, 
                  current_time.minute, 
                  current_time.day, month,  
                  current_time.year,
                  current_temperature,
                  current_humidiy,
                  weather_description,
                  get_location.get_current_location()))

elif current_time.hour > 12:
    print("Hello Sir, A very good evening to you! It is {} hundred {} hours on {} of {} {} with {} degree celcius, {} percent humidity and {} here in {}"
          .format(current_time.hour, 
                  current_time.minute, 
                  current_time.day, month,  
                  current_time.year,
                  current_temperature,
                  current_humidiy,
                  weather_description,
                  get_location.get_current_location()))
    tts.speak("Hello Sir, A very good evening to you! It is {} hundred {} hours on {} of {} {} with {} degree celcius, {} percent humidity and {} here in {}"
          .format(current_time.hour, 
                  current_time.minute, 
                  current_time.day, month,  
                  current_time.year,
                  current_temperature,
                  current_humidiy,
                  weather_description,
                  get_location.get_current_location()))

else: 
    print("Hello Sir, A very good afternoon to you! It is {} hundred {} hours on {} of {} {} with {} degree celcius, {} percent humidity and {} here in {}"
              .format(current_time.hour, 
                      current_time.minute, 
                      current_time.day, month,  
                      current_time.year,
                      current_temperature,
                      current_humidiy,
                      weather_description,
                      get_location.get_current_location()))
    tts.speak("Hello Sir, A very good afternoon to you! It is {} hundred {} hours on {} of {} {} with {} degree celcius, {} percent humidity and {} here in {}"
          .format(current_time.hour, 
                  current_time.minute, 
                  current_time.day, month,  
                  current_time.year,
                  current_temperature,
                  current_humidiy,
                  weather_description,
                  get_location.get_current_location()))
    
hot_word = ""
if len(hot_word) > 0:
    print("Please activate the assistant using your hot word!")
    stt.speechToText()
else:
    tts.speak("You can set your hot word in order to activate me later on!")
    tts.speak("What would you like to set your hot name as?")
    hot_word = stt.speechToText()
    tts.speak("I have set your hot word as "+hot_word)
#Detect Intent and integrated with the funnctionality files
    
    
