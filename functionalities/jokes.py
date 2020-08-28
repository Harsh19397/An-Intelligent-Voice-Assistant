import pyjokes
from google_apis_speech_text_conversion import TextToSpeech as tts

def get_jokes(assistant_name):
    assistant_name = "Gideon"
    joke = pyjokes.get_joke()
    print("{}: ".format(assistant_name) + joke)
    tts.speak(joke)