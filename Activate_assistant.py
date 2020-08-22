from record_audio import record_audio
from google_apis_speech_text_conversion import TextToSpeech as tts
from speaker_identification import get_speaker_identity

def hot_word_activation(User_name, assistant_name):
    tts.speak("{}: Please say your hot word to activate!".format(assistant_name))
    print("{}: Please say your hot word to activate!".format(assistant_name))
    record_audio("validation_audio")
    
    result = get_speaker_identity(User_name)
    
    if result:
        return True
            
    else:
        return False
    