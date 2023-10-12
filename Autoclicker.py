import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

print("AutoClicker by Danyil Niemtsov\n")
print("-> Settings: \n")
print("   delay: 0.1s")
print("   z = Resume / pause")
print("   close terminal = Exit\n")
print("-----------------------------------------------------")

TOGGLE_KEY = KeyCode(char="z")
clicking = False
mouse = Controller()
last_state = None

def clicker():
    global last_state
    while True:
        if clicking:
            if last_state != "[resumed]":
                print("[resumed]")
                last_state = "[resumed]"
            mouse.click(Button.left, 1)
        else:
            if last_state != "[paused]":
                print("[paused]")
                last_state = "[paused]"
        time.sleep(0.1)

def toggle_event(key):
    global clicking
    if key == TOGGLE_KEY:
        clicking = not clicking

click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()