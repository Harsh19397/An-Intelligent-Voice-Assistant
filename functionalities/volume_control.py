import pyautogui
from google_apis_speech_text_conversion import SpeechToText as stt
from google_apis_speech_text_conversion import TextToSpeech as tts

def get_intent_of_user(assistant_name, query):
    decrease = ["dim", "decrease", "reduce", "dull", "lessen", "decline", "cutdown", "lower", "minimize",  "dimnish", "drop", "cut"]
    increase = ["increase", "augment", "surge", "escalate", "intensify", "raise", "boost"]
    mute = ["mute", "silent", "zero", "zap", "silence", "off"]

    if any(ele in query for ele in decrease):
        return ['decrease' for ele in decrease if(ele in query)][0]
    elif any(ele in query for ele in increase):
        return ['increase' for ele in increase if(ele in query)][0]
    elif any(ele in query for ele in mute):
        return ['mute' for ele in mute if(ele in query)][0]
    else:
        print("{}: What do you want me to do with the volume?".format(assistant_name))
        tts.speak("What do you want me to do with the volume?(decrease/increase/mute)")
        ans = stt.speechToText()
        return ans


def increase_volume():
    for i in range(10):
        pyautogui.press('volumeup')

def decrease_volume():
    for i in range(8):
        pyautogui.press('volumedown')

def mute_unmute_volume():
    pyautogui.press('volumemute')

def volume_control(assistant_name, query):

    intent_user = get_intent_of_user(assistant_name, query)

    if intent_user == 'decrease':
        decrease_volume()
    elif intent_user == 'increase':
        increase_volume()

    elif intent_user == 'mute':
        mute_unmute_volume()

    else:
        query += intent_user
        volume_control(assistant_name, query)