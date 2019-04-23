#coding:utf-8

import requests
import config
import pykeyboard
import ctypes, pyperclip
from time import *


class Fxxku(object):
    
    url = ""
    interval = 1
    user32 = ctypes.windll.user32

    def __init__(self):
        self.url = config.URL
        self.interval = config.INTERVAL

    def empty_clipboard(self):
        self.user32.OpenClipboard(0)
        self.user32.EmptyClipboard()
        self.user32.CloseClipboard()

    def write_clipboard(self, data):
        pyperclip.copy(data)

    def get_material(self, interval):
        material = []
        self.interval = interval
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # disable warning of https
        for i in range(self.interval):
            r = requests.get(self.url, verify=False)
            material.append(r.text)
        return material

    def response(self, interval=config.INTERVAL):
        '''
        Use clipboard to solve problem of chinese coding
        '''
        material = self.get_material(interval)
        keyboard = pykeyboard.PyKeyboard()
        for m in material:
            self.write_clipboard(m)
            keyboard.tap_key(keyboard.enter_key)
            
            keyboard.press_key(keyboard.control_key)
            keyboard.tap_key('V')
            keyboard.release_key(keyboard.control_l_key)
            keyboard.tap_key(keyboard.enter_key)
            sleep(0.5)

class Overwatch(Fxxku):

    def __init__(self):
        pass

    def response(self, interval=config):
        material = self.get_material(interval)
        keyboard = pykeyboard.PyKeyboard()
        for m in material:
            self.write_clipboard(m)
            keyboard.tap_key(keyboard.enter_key)
            keyboard.press_key(keyboard.control_l_key)
            keyboard.tap_key('V')
            keyboard.release_key(keyboard.control_key)
            keyboard.tap_key(keyboard.enter_key)

if __name__ == '__main__':
    fxxku = Fxxku()
    fxxku.response()