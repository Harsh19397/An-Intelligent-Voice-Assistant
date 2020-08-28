import json
import requests, time
from google_apis_speech_text_conversion import TextToSpeech as tts
from google_apis_speech_text_conversion import SpeechToText as stt

def get_news(assistant_name, query):
    f = open('news.json', 'r')
    API_KEY = json.load(f)["key"]
    f.close()
    url_first_half = "http://newsapi.org/v2/everything?q="
    url_second_half = "&from=2020-07-28&sortBy=publishedAt&apiKey="+API_KEY

    query = query.lower()
    query = query.split()
    trigger_words = ['on', 'about', 'for']

    print("{}: Here goes your news:".format(assistant_name))
    tts.speak("Here goes your news: ")

    #Extracting the trigger words
    for word in trigger_words:
        try:
            index_val = query.index(word)
            break
        except:
            continue

    if 'index_val' in locals():
        query = query[index_val+1:]

        #Constructing the URL
        for x in query:
            url_first_half += x + "+"
        url_first_half[:-1]
        URL = url_first_half + url_second_half

        r = requests.get(url = URL)
        data = r.json()

        for i in range(3):
            tts.speak(data["articles"][i]["description"])
            time.sleep(2)

    elif 'headlines' in query:
        URL = 'http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey='+API_KEY

        r = requests.get(url = URL)
        data = r.json()

        for i in range(3):
            tts.speak(data["articles"][i]["description"])
            time.sleep(2)

    else:
        print("{}: What do you want to listen about in news section?".format(assistant_name))
        tts.speak("What do you want to listen about in news section?")
        text = stt.speechToText()
        for x in text:
            url_first_half += x + "+"
        url_first_half[:-1]
        URL = url_first_half + url_second_half

        r = requests.get(url = URL)
        data = r.json()

        for i in range(3):
            tts.speak(data["articles"][i]["description"])
            time.sleep(2)
