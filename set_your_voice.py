from record_audio import record_audio
from google_apis_speech_text_conversion import TextToSpeech as tts

def set_your_audio(User_name, assistant_name):
    #Make your assistant personal by storing your audio
    tts.speak("Sir! Please say activate {} so that we can save your audio and later only you will be able to activate and use your assistant.".format(assistant_name))
    print("{} : Sir! Please say activate {} so that we can save your audio and later only you will be able to activate and use your assistant.".format(assistant_name, assistant_name))
    record_audio(User_name+"1")
    
    #Saving second file
    tts.speak("Once more please.")
    print("{}: Once more please".format(assistant_name))
    record_audio(User_name+"2")
    
    #Saving third file
    tts.speak("Just one last time")
    print("{}: Just one last time".format(assistant_name))
    record_audio(User_name+"3")
