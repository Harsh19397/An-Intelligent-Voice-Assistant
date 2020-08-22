from functionalities import datetime, get_location, weatherInfor
from google_apis_speech_text_conversion import SpeechToText as stt
from google_apis_speech_text_conversion import TextToSpeech as tts

    

def startup_message():
    #Start_up
    current_time, month = datetime.get_date_time()
    current_temperature, current_pressure, current_humidiy, weather_description = weatherInfor.get_weather(get_location.get_current_location())
    
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
        
def setting_up_hot_word(hot_word):    
    
    if len(hot_word) > 0:
        print("Please activate the assistant using your hot word!")
        stt.speechToText()
    else:
        tts.speak("You can set your hot word in order to activate me later on!")
        tts.speak("What would you like to set your hot name as?")
        hot_word = stt.speechToText()
        tts.speak("I have set your hot word as "+hot_word)
    
    return hot_word