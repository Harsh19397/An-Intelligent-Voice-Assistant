import pyautogui

def increase_voulume():
    for i in range(10):
        pyautogui.press('volumeup')
        
def decrease_volume():
    for i in range(8):
        pyautogui.press('volumedown')
        
def mute_unmute_volume():
    pyautogui.press('volumemute')