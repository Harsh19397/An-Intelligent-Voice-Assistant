from google_apis_speech_text_conversion import TextToSpeech as tts
import re
import webbrowser
from google_apis_speech_text_conversion import SpeechToText as stt
from functionalities import get_location

def show_route(assistant_name, query):
    assistant_name = "Gideon"
    url = 'https://www.google.com/maps/dir/'
    query = query.lower()
    clean = re.sub(r'[^ a-z A-Z 0-9]', " ", query)
    clean = clean.split()
    
    to_check = 0
    from_check = 0

    try:    
        to_loc = clean.index('to')
    except:
        print("{}: For which destination do you want to have route for?".format(assistant_name))
        tts.speak("For which destination do you want to have route for?")
        destination = stt.speechToText()
        to_check = 1
        
    try:
        from_loc = clean.index('from')
    except:
        print("{}: What is your starting point?".format(assistant_name))
        tts.speak("What is your starting point?")
        start_point = stt.speechToText()
        from_check = 1
    
    if to_check == 0:
        #destination
        if from_check == 0:
            if from_loc > to_loc:
                destination = clean[to_loc+1:from_loc]
            else:
                destination = clean[to_loc+1:]
        else:
            destination = clean[to_loc+1:]
    
    if from_check == 0:
        if to_check == 0:
            #Start point
            if from_loc > to_loc:
                start_point = clean[from_loc+1:]
            else:
                start_point = clean[from_loc+1:to_loc]
        else:
            start_point = clean[from_loc+1:]
    
    
    if start_point[0] == 'here':
        lat, lon = get_location.get_lat_lon()
        start_point = [lat+','+lon]
        
    #forming the URL
    #Concatenatiing the start point
    for s in start_point:
        url += s + '+'
    url = url[:-1]
    url += '/'
    #Concatenating the destination
    for d in destination:
        url += d + '+'
    url = url[:-1]
    
    #Openning up youtube in the chrome browser 
    webbrowser.register('chrome',
                        None,
                        webbrowser.BackgroundBrowser("C:/Program Files (x86)/Google/Chrome/Application/chrome"))
    webbrowser.get('chrome').open(url)
    
    
