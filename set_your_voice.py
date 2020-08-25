from record_audio import record_audio
from google_apis_speech_text_conversion import TextToSpeech as tts

def set_your_audio(User_name):
    #Make your assistant personal by storing your audio
    tts.speak("Sir! Please say your password so that we can save your audio and later only you will be able to activate and use your assistant.")
    print("Sir! Please say your password so that we can save your audio and later only you will be able to activate and use your assistant.")
    record_audio(User_name)
    
