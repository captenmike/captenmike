#!/usr/bin/env python

import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

print("Toggle on/off key by pressing '='")
print("Enjoy ;)")

TOGGLE_KEY = KeyCode(char="=")

clicking = False
mouse = Controller()

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
            mouse.click(Button.left, 1)
            mouse.click(Button.left, 1)
            mouse.click(Button.left, 1)
            mouse.click(Button.left, 1)
            mouse.click(Button.left, 1)
        time.sleep(0.000001)
        
def toggle_even(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking

click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_even) as listener:
    listener.join()