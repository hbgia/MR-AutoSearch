from pynput.keyboard import Controller, Key
from pynput.mouse import Controller as MouseController
kb = Controller()
mouse = MouseController()


# import subprocess
# def open_MS_Edge():
#     subprocess.Popen(["msedge"])
import os
import shutil
import subprocess
from typing import Optional, Sequence
def open_ms_edge(args: Optional[Sequence[str]] = None, url: Optional[str] = None) -> subprocess.Popen:
    """
    Open Microsoft Edge and return the Popen process object.
    - args: extra command-line arguments for msedge
    - url: optional URL to open
    """
    exe = shutil.which("msedge")
    if not exe:
        candidates = [
            r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
            r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        ]
        for p in candidates:
            if os.path.exists(p):
                exe = p
                break

    cmd = [exe] if exe else None
    if url:
        if cmd:
            cmd.append(url)
        else:
            # fallback to shell start if no executable found
            return subprocess.Popen(["start", url], shell=True)

    if args:
        if cmd:
            cmd.extend(args)

    if not cmd:
        # last resort: use start to open Edge (Windows)
        return subprocess.Popen(["start", "msedge"], shell=True)

    return subprocess.Popen(cmd)

    
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
