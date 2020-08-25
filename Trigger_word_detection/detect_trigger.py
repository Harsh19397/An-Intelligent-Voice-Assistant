import speech_recognition as sr

r = sr.Recognizer()

def trigger_word_detection(hot_word):
    print("Try saying '{}!'".format(hot_word))
    while True:
        try:    
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                
                #print("Please say something...")
                r.pause_threshold = 1
                audio = r.listen(source)
                
                if hot_word.lower() in r.recognize_google(audio).lower():
                    print("Activated!")
                    return True
                
                else:
                    continue
        except:
            continue

