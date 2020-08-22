import speech_recognition as sr


def speechToText():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        
        print("Please say something...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
        try:
            print("Recognizing...")
            return r.recognize_google(audio), audio
            
        except Exception as e:
            print("Error: "+str(e))
        return "Error"
    


