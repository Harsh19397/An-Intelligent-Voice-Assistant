import ctypes
from google_apis_speech_text_conversion import SpeechToText as stt
from google_apis_speech_text_conversion import TextToSpeech as tts
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import glob
import os
import webbrowser, time
import pyautogui
import random

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
    clean = re.sub(r'would', "", clean)
    clean = re.sub(r'like', "", clean)
    clean = re.sub(r'set', "", clean)
    clean = re.sub(r'wallpaper', "", clean)
    clean = re.sub(r'background', "", clean)
    clean = re.sub(r'change', "", clean)
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
    time.sleep(3)
    #Setting the orientation
    landscape_options = pyautogui.locateOnScreen('./functionalities/images/landscape.png')
    landscape_options_as_location = pyautogui.center(landscape_options)
    pyautogui.click(landscape_options_as_location)
    time.sleep(1)
    x_land, y_land = pyautogui.position()
    pyautogui.click(x_land, y_land+80)
    #Scrolling a bit for random selection
    random_scroll = random.randint(1, 10)
    pyautogui.scroll(-500*random_scroll)
    time.sleep(2)
    random_x = random.randint(350, 700)
    pyautogui.click(x = random_x, y=450)
    time.sleep(2)
    #Saving the image
    download_image = pyautogui.locateOnScreen('./functionalities/images/download.png')
    download_image_as_location = pyautogui.center(download_image)
    pyautogui.click(download_image_as_location)
    #Setting up the background
    time.sleep(4)
    list_of_files = glob.glob(r'C:\Users\Harsh Parashar\Downloads\*')
    latest_file = max(list_of_files, key=os.path.getctime)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, latest_file , 0)
    print("{}: Background has been set.".format(assistant_name))
    tts.speak("Background has been set.")