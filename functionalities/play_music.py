from google_apis_speech_text_conversion import TextToSpeech as tts
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import webbrowser, time
import pyautogui

def play_music(assistant_name, query):
    url ="https://open.spotify.com/search/"
    #query = "Please play sugar by maroon 5 on spotify"
    query = query.lower()
    #Cleaning the text
    clean = re.sub(r'[^ a-z A-Z 0-9]', " ", query)
    clean = re.sub(r'play', "", clean)
    clean = re.sub(r'please', "", clean)
    clean = re.sub(r'would', "", clean)
    clean = re.sub(r'spotify', "", clean)
    clean = re.sub(r'music player', "", clean)    
    word_tokens = word_tokenize(clean)
    
    #Removing the stopwords
    stop_words = set(stopwords.words('english'))
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    
    #Getting the URL ready
    uri = ""
    for x in filtered_sentence:
        uri = uri + x + " "
    for x in uri.split():
        url += x + '%20'  
    url = url[:-3]
    
    #Openning up youtube in the chrome browser 
    webbrowser.register('chrome',
                        None,
                        webbrowser.BackgroundBrowser("C:/Program Files (x86)/Google/Chrome/Application/chrome"))
    webbrowser.get('chrome').open(url)
    #print("{}: Your song {} will be now played.".format(assistant_name, uri))    
    #tts.speak("Your song {} will be now played.".format(uri))
    #playing the music
    print("{}: Playing your song!".format(assistant_name))
    tts.speak("Playing your song!")
    time.sleep(5)
    pyautogui.click(x = 503, y=289)    
    