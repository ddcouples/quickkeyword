#!/usr/bin/python3
# Filename: support.py
from pynput import keyboard
from pynput.keyboard import Key, Controller
import time
curkeyboard = Controller()
midTime=0.05
fastTime=0.02
slowTime=0.1
def keyboardPress(par):
  curkeyboard.press(par)
  time.sleep(midTime)
  curkeyboard.release(par)
# wasd 上下左右 jkli：ABCD键位
orderListconfig=[("u", 'dsdasaddaajj'), ('o', 'asadsdaaddjj'), ('h', 'sksk')]
replaceConfig=[(";", 'jkl')]

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
        print('key {0} pressed'.format(
            key.char))
        for i in range(len(replaceConfig)):
            (hotkey, keyList)=replaceConfig[i]
            if (key.char == hotkey):
                print('replaceConfig bigo {0}'.format(hotkey))
                for charIndex in range(len(keyList)):
                    _curKey = keyList[charIndex]
                    curkeyboard.press(_curKey)
    except AttributeError:
        print('special {0} pressed'.format(
            key))

def on_release(key):
    try:
        print('key {0} released'.format(
            key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False
        for i in range(len(replaceConfig)):
            (hotkey, keyList)=replaceConfig[i]
            if (key.char == hotkey):
                print('replaceConfig bigo {0}'.format(hotkey))
                for charIndex in range(len(keyList)):
                    _curKey = keyList[charIndex]
                    curkeyboard.release(_curKey)
        for i in range(len(orderListconfig)):
            (hotkey, keyList)=orderListconfig[i]
            if (key.char == hotkey):
                print('bigo')
                # keyList() 
                curDist={}
                for _charIndex in range(len(keyList)):
                    curDist[keyList[_charIndex]] = 0
                for charIndex in range(len(keyList)):
                    _curKey = keyList[charIndex]
                    print(_curKey)
                    curDist[_curKey] += 1
                    if curDist[_curKey] % 2 == 0:
                        curkeyboard.release(_curKey)
                    else:
                        curkeyboard.press(_curKey)
                    time.sleep(fastTime)
    except AttributeError:
        print('special key {0} release'.format(
            key))
