from pynput.keyboard import Controller, Key
from pynput.mouse import Controller as MouseController
kb = Controller()
mouse = MouseController()


import subprocess
def open_MS_Edge():
    subprocess.Popen(["msedge"])
    
    
def start_search_in_address_bar():
    """
    press Ctrl + K to start searching in address bar. Note: MUST BE EXECUTED WHILE EDGE IS IN FOCUS.
    """
    kb.press(Key.ctrl)
    kb.press('k')
    kb.release('k')
    kb.release(Key.ctrl)


import time
def type_each_char(text:str):
    for char in text:
        kb.press(char)
        kb.release(char)
        time.sleep(0.02)


def press_enter():
    kb.press(Key.enter)
    

def close_Edge():
    subprocess.Popen(["msedge"]).terminate()