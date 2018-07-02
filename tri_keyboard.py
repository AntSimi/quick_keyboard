#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from math import ceil


class Application(tk.Frame):
    ALPHAS = (('abc', 'def', 'ghi'), ('jkl', 'mno', 'pqr'), ('stu', 'wvx', 'yz_'))
    NB_LETTER = 30
    BUTTONS = {
        # ~ '7' : 0, '1' : 0, 'y' : 0,
        # ~ '8' : 1, '5' : 1, '2' : 1, 'u' : 1,
        # ~ '9' : 2, '6' : 2, '3' : 2, 'i' : 2,
        # ~ ' ' : 3,'0' : 3,
        # ~ 'f' : 0, 'g' : 0, 
        # ~ 'u' : 1, 'i' : 1,
        # ~ 'l' : 2, 'm' : 2,
        # ~ 'z' : 3,'e' : 3,
        'f' : 0,
        'u' : 1,
        'l' : 2,
        'z' : 3,
        }
    FONTSIZE=40
    
    def createWidgets(self):
        self.display = tk.Label(self, font=("Courier", self.FONTSIZE))
        self.display.pack({'side': 'top'})
        self.buttons = list()
        for group in self.ALPHAS:
            self.buttons.append(tk.Label(self, font=("Courier", self.FONTSIZE)))
        self.standard_alpha()
        
        for button in self.buttons:
            button.pack({'side' : 'left'})

    def __init__(self, master=None):
        super(Application, self).__init__(master)
        self.pack()
        self.createEvent()
        self.createWidgets()
        self.accum = ''
        self.series = None

    def createEvent(self):
        self.master.bind("<KeyRelease>", self.key)

    def standard_alpha(self):
        for j, button in enumerate(self.buttons):
            button['text'] = '  ' + ''.join(self.ALPHAS[j]).upper() + '  '

    def key(self, event):
        if event.char in self.BUTTONS.keys():
            i = self.BUTTONS[event.char]
            if i == 3:
                if self.series is None:
                    self.accum = self.accum[:-1]
                    self.display['text'] = self.accum[-self.NB_LETTER:]
                else:
                    self.series=None
                    self.standard_alpha()
            else:
                if self.series is None :
                    self.series=self.ALPHAS[i]
                    for j, button in enumerate(self.buttons):
                        button['text'] = '  %s  ' % self.series[j].upper()
                elif isinstance(self.series, tuple):
                    self.series=self.series[i]
                    for j, button in enumerate(self.buttons):
                        button['text'] = '  %s  ' % self.series[j].upper()
                else:
                    self.accum += self.series[i].replace('_', ' ')
                    self.display['text'] = self.accum[-self.NB_LETTER:]
                    self.series=None
                    self.standard_alpha()
            
if __name__ == '__main__':
    app = Application()
    app.mainloop()
