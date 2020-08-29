import os
from google_apis_speech_text_conversion import TextToSpeech as tts
from google_apis_speech_text_conversion import SpeechToText as stt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

def find_files(filename, search_path):
   result = []

# Wlaking top-down from the root
   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   return result


def launch_application(assistant_name, query):
    query = query.lower()

    #Cleaning the text
    clean = re.sub(r'[^ a-z A-Z 0-9]', " ", query)
    clean = re.sub(r'open', "", clean)
    clean = re.sub(r'please', "", clean)
    clean = re.sub(r'would', "", clean)
    clean = re.sub(r'launch', "", clean)
    clean = re.sub(r'could', "", clean)
    word_tokens = word_tokenize(clean)

    #Removing the stopwords
    stop_words = set(stopwords.words('english'))
    filtered_sentence = [w for w in word_tokens if not w in stop_words]

    if len(filtered_sentence) == 1:
        app = filtered_sentence[0]
        app_name = app + ".exe"
        file_path = find_files(app_name,r"C:\Program Files (x86)")
        if file_path:
            print("{}: Launching the application!".format(assistant_name))
            tts.speak("Launching the application!")
            os.startfile(file_path[0])
        else:
            print("{}: I cannot find {} in the system. Please proceed to launch it mannually. ".format(assistant_name, app))
            tts.speak("I cannot find {} in the system. Please proceed to launch it mannually.".format(app))

    else:
        print("{}: I could not really understand you earlier. Which application would you like me to open?".format(assistant_name))
        tts.speak("I could not really understand you earlier. Which application would you like me to open?")
        app = stt.speechToText()
        app_name = app + ".exe"
        file_path = find_files(app_name,r"C:\Program Files (x86)")
        if file_path:
            print("{}: Launching the application!".format(assistant_name))
            tts.speak("Launching the application!")
            os.startfile(file_path[0])
        else:
            print("{}: I cannot find {} in the system. Please proceed to launch it mannually. ".format(assistant_name, app))
            tts.speak("I cannot find {} in the system. Please proceed to launch it mannually.".format(app))
