import ctypes
from google_apis_speech_text_conversion import SpeechToText as stt
from google_apis_speech_text_conversion import TextToSpeech as tts
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import webbrowser, time
import pyautogui

def set_Background_Image(assistant_name):
    print("{}: What background image you want to set?".format(assistant_name))
    tts.speak("What background image you want to set?")
    text = stt.speechToText()
    url ="https://unsplash.com/s/photos/"
    text = text.lower()
    
    #Cleaning the text
    clean = re.sub(r'[^ a-z A-Z 0-9]', " ", text)
    clean = re.sub(r'search', "", clean)
    clean = re.sub(r'please', "", clean)
    word_tokens = word_tokenize(clean)
    
    #Removing the stopwords
    stop_words = set(stopwords.words('english'))
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    
    #Getting the URL ready
    uri = ""
    for x in filtered_sentence:
        uri = uri + x + " "
    for x in uri.split():
        url += x + '-'  
    url = url[:-1]
    
    #Openning up youtube in the chrome browser 
    webbrowser.register('chrome',
                        None,
                        webbrowser.BackgroundBrowser("C:/Program Files (x86)/Google/Chrome/Application/chrome"))
    webbrowser.get('chrome').open(url)
    
    #Saving the first image
    time.sleep(5)
    pyautogui.click(x = 200, y=600, button='right')
    time.sleep(3)
    save_image = pyautogui.locateOnScreen('./functionalities/images/save_image_as.png')
    save_image_as_location = pyautogui.center(save_image)
    pyautogui.click(save_image_as_location)
    time.sleep(5)
    pyautogui.write('background_set_{}'.format(text)) 
    pyautogui.press('enter')
    time.sleep(5)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, r'C:\Users\Harsh Parashar\Downloads\background_set_{}.jfif'.format(text) , 0)
    print("{}: Background has been set.".format(assistant_name))
    tts.speak("Background has been set.")