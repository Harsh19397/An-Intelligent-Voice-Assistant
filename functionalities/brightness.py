import wmi
from google_apis_speech_text_conversion import SpeechToText as stt
from google_apis_speech_text_conversion import TextToSpeech as tts


def get_intent_of_user(assistant_name, query):
    decrease = ["dim", "decrease", "reduce", "dull", "lessen", "decline", "cutdown", "lower", "minimize",  "dimnish", "drop", "cut"]
    increase = ["increase", "augment", "surge", "escalate", "intensify", "raise", "boost"]
    high = ["shoot up", "max", "max out", "highest", "max level", "maximize"]

    if any(ele in query for ele in decrease):
        return ['decrease' for ele in decrease if(ele in query)][0]
    elif any(ele in query for ele in increase):
        return ['increase' for ele in increase if(ele in query)][0]
    elif any(ele in query for ele in high):
        return ['max' for ele in high if(ele in query)][0]
    else:
        print("{}: What do you want me to do with the brightness?".format(assistant_name))
        tts.speak("What do you want me to do with the brightness?(decrease/increase/max)")
        ans = stt.speechToText()
        return ans

def brightness_control(assistant_name, query):

    intent_user = get_intent_of_user(assistant_name, query)

    if intent_user == 'decrease':
        wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(25, 0)

    elif intent_user == 'increase':
        wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(70, 0)

    elif intent_user == 'max':
        wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(100, 0)

    else:
        query += intent_user
        brightness_control(assistant_name, query)


