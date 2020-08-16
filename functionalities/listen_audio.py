import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        
        print("Please say something...")
        r.pause_threshold = 1
        audio = r.listen(source)
        return audio