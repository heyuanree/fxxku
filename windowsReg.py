#coding:utf-8

"""
This module config hotkey and other windows configuration such as startuo.
"""

import config
from fxxku import  Fxxku
from pyhooked import Hook, KeyboardEvent

class WindowsReg(object):
    
    hotkey_leader = config.HOTKEY_LERDER
    hotkey_fun = config.HOTKET_FUN
    hk = None
    fk = None

    def __init__(self):
        self.hk = Hook()
        self.fk = Fxxku()

    def register_startup(self):
        pass
    
    def release_startup(self):
        pass

    def register_hotkey(self):
        self.hk.handler = self.handler_event
        self.hk.hook()

    def release_hotkey(self):
        self.hk.stop()

    def set_taskbar(self):
        pass

    def handler_event(self, args):
        if isinstance(args, KeyboardEvent):
            if args.current_key == self.hotkey_fun and args.event_type == 'key down' and self.hotkey_leader in args.pressed_key:
                self.fk.response()
            elif args.current_key == 'Q' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
                self.release_hotkey()
                self.fk.empty_clipboard()