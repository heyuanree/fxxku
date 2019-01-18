# coding: utf-8

import config
import tkinter as tk
from fxxku import Fxxku
from windowsReg import WindowsReg

windows_reg = WindowsReg()

class Fxxu_GUI(object):
    
    root = None
    
    label_url = None
    label_interval = None
    label_hotkey = None
    
    entry_url = None
    entry_interval = 1
    entry_hotkey = None
    entry_url_var = None
    entry_hotkey_var = None
    entry_interval_var = None

    button_start = None
    button_pause = None


    def __init__(self):
        self.root = tk.Tk()
        self.label_url = tk.Label(self.root, text=u'URL')
        self.label_url.grid(row=0)
        self.label_interval = tk.Label(self.root, text=u'次数')
        self.label_interval.grid(row=1)
        self.label_hotkey = tk.Label(self.root, text=u'热键')
        self.label_hotkey.grid(row=2)

        self.entry_hotkey_var = tk.Variable()
        self.entry_interval_var = tk.Variable()
        self.entry_url_var = tk.Variable()
        self.entry_hotkey_var.set(config.HOTKEY_LERDER + '+' + config.HOTKET_FUN)
        self.entry_interval_var.set(config.INTERVAL)
        self.entry_url_var.set(config.URL)
        self.entry_url = tk.Entry(self.root, textvariable=self.entry_url_var)
        self.entry_url.grid(row=0, column=1)
        self.entry_interval = tk.Entry(self.root, textvariable=self.entry_interval_var)
        self.entry_interval.grid(row=1, column=1)
        self.entry_hotkey = tk.Entry(self.root, textvariable=self.entry_hotkey_var)
        self.entry_hotkey.grid(row=2, column=1)

        self.button_start = tk.Button(self.root, text=u'Start', command=self.start)
        self.button_start.grid(row=3, column=0)
        self.button_pause = tk.Button(self.root, text=u'Pause', command=self.pause)
        self.button_pause.grid(row=3, column=1)

        self.root.mainloop()


    def set_root_window(self):
        self.root.title(u'Fxxku')
        self.root.geometry('400*400')
        self.root.resizable(width=True, height=True)

    def save_config(self, **kwargs):
        self.entry_interval_var = kwargs['entry_interval_var']
        self.entry_hotkey_var = kwargs['entry_hotkey_var']
        self.entry_url_var = kwargs['entry_url_var']

    def start(self):
        self.save_config(
            entry_interval_var = self.entry_interval_var.get(),
            entry_hotkey_var = self.entry_hotkey_var.get(),
            entry_url_var = self.entry_url_var.get()
        )
        windows_reg.register_hotkey()

    def pause(self):
        windows_reg.release_hotkey()

if __name__ == '__main__':
    fg = Fxxu_GUI()