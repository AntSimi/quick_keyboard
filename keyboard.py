#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from math import ceil


class Application(tk.Frame):
    DOIGTS = ('Pouce', 'Index', 'Majeur', 'Annul.', 'Auri.')
    ALPHAS = ('abcde', 'fghij', 'klmno', 'pqrst', 'uvxy_')
    ALPHAS2 = ('wz!?.', '01234', '56789', '><=+-', '():,_')
    BUTTONS = {
        ' ' : 0,
        'y' : 1,
        'u' : 2,
        'i' : 3,
        'l' : 4,
        't' : 5,
        'g' : 6,
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
        self.master.bind("<Key>", self.key)

    def standard_alpha(self):
        for j, button in enumerate(self.buttons):
            button['text'] = '  ' + ''.join(self.ALPHAS[j].upper()) + '  '

    def key(self, event):
        if event.char in self.BUTTONS.keys():
            i = self.BUTTONS[event.char]
            if i == 6:
                self.ALPHAS, self.ALPHAS2 = self.ALPHAS2, self.ALPHAS
                self.series=None
                self.standard_alpha()
            elif i == 5:
                if self.series is None:
                    self.accum = self.accum[:-1]
                    self.display['text'] = self.accum
                else:
                    self.series=None
                    self.standard_alpha()
            else:
                if self.series is None :
                    self.series=self.ALPHAS[i]
                    for j, button in enumerate(self.buttons):
                        button['text'] = '  %s  ' % self.series[j].upper()
                else:
                    self.accum += self.series[i].replace('_', ' ')
                    self.display['text'] = self.accum
                    self.series=None
                    self.standard_alpha()
            
if __name__ == '__main__':
    app = Application()
    app.mainloop()
