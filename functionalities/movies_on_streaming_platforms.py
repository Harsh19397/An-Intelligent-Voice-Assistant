#Opening Movies on various online streaming platforms like Netflix, Prime and hotstar
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import webbrowser
from google_apis_speech_text_conversion import SpeechToText as stt
from google_apis_speech_text_conversion import TextToSpeech as tts

def remove_stop_words(query):
    stop_words = set(stopwords.words('english'))

    word_tokens = word_tokenize(query)

    filtered_sentence = [w for w in word_tokens if not w in stop_words]

    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    return filtered_sentence


def play_on_Netflix(query, assistant_name):
    query = query.lower()
    query = query.replace("play", "")
    query = query.replace("netflix", "")
    query = remove_stop_words(query)
    url = "https://www.netflix.com/search?q="
    for s in query:
        url = url + s + "+"
    url = url[:-1]
    print("{}: Here you go.".format(assistant_name))
    tts.speak("Here you go!")

    webbrowser.get('chrome').open(url)

def play_on_Prime(query, assistant_name):
    query = query.lower()
    query = query.replace("play", "")
    query = query.replace("prime", "")
    query = query.replace("video", "")
    query = remove_stop_words(query)
    url = "https://www.primevideo.com/search/ref=atv_nb_sr?phrase="
    for s in query:
        url = url + s + "+"
    url = url[:-1]
    url = url + "&ie=UTF8"
    print("{}: Here you go.".format(assistant_name))
    tts.speak("Here you go!")

    webbrowser.get('chrome').open(url)

def play_on_Hotstar(query, assistant_name):
    query = query.lower()
    query = query.replace("play", "")
    query = query.replace("hotstar", "")
    query = query.replace("Disney", "")
    query = remove_stop_words(query)
    url = "https://www.hotstar.com/in/search?q="
    for s in query:
        url = url + s + "%20"
    url = url[:-3]
    print("{}: Here you go.".format(assistant_name))
    tts.speak("Here you go!")

    webbrowser.get('chrome').open(url)

def stream_movie(assistant_name, query):

    if 'netflix' in query:
        play_on_Netflix(query, assistant_name)
    elif 'prime' in query:
        play_on_Prime(query, assistant_name)
    elif 'hotstar' in query:
        play_on_Hotstar(query, assistant_name)
    else:
        print("{}: On which platform do you want me to play the movie?".format(assistant_name))
        tts.speak("On which platform do you want me to play the movie?")
        ans = stt.speechToText()
        query = query + ans
        stream_movie(assistant_name, query)