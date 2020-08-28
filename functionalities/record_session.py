import pyautogui
import os
import time
from google_apis_speech_text_conversion import TextToSpeech as tts

def record_session(assistant_name):
    #Install bandicam
    os.startfile(r'C:\Program Files (x86)\Bandicam\bdcam_nonadmin.exe')
    time.sleep(10)
    full_screen_selection = pyautogui.locateOnScreen('./functionalities/images/full_screen_selection.png')
    full_screen_selection_location = pyautogui.center(full_screen_selection)
    pyautogui.click(full_screen_selection_location)
    time.sleep(2)
    full_screen = pyautogui.locateOnScreen('./functionalities/images/full_screen.png')
    full_screen_location = pyautogui.center(full_screen)
    pyautogui.click(full_screen_location)
    time.sleep(1)
    print("{}: Recording the session. Stop mannually when you are done".format(assistant_name))
    tts.speak("Recording the session. Stop mannually when you are done")
    record = pyautogui.locateOnScreen('./functionalities/images/record.png')
    record_location = pyautogui.center(record)
    pyautogui.click(record_location)