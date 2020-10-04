#!/usr/bin/python3
# Filename: support.py
from pynput import keyboard
from pynput.keyboard import Key, Controller
import time
curkeyboard = Controller()

config=[("j", "g")]

def keyboardPress(par):
  curkeyboard.press(par)
  time.sleep(0.05)
  curkeyboard.release(par)

def init():
  keyboard_listener=keyboard.Listener(on_press=on_press,on_release=on_release)
  # mouse_listener=mouse.Listener(on_click=on_click,on_move=on_move,on_scroll=on_scroll)
  lst=[keyboard_listener]

  for t in lst:
      t.start()

  for t in lst:
      t.join()
  
def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('alphanumeric {0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    try:
      for i in range(len(config)):
        (hotkey, keyList)=config[i]
        if (key.char == hotkey):
            print('bigo')
            for charIndex in range(len(keyList)):
                print(keyList[charIndex])
                keyboardPress(keyList[charIndex])
                time.sleep(0.05)
    except AttributeError:
        print('special key {0} release'.format(
            key))
    
   
# def on_move(x, y):
#     print('Pointer moved to {0}'.format(
#         (x, y)))

# def on_click(x, y, button, pressed):
#     print('{0} at {1}'.format(
#         'Pressed' if pressed else 'Released',
#         (x, y)))
#     if not pressed:
#         # Stop listener
#         return False

# def on_scroll(x, y, dx, dy):
#     print('Scrolled {0} at {1}'.format(
#         'down' if dy < 0 else 'up',
#         (x, y)))

# Collect events until released