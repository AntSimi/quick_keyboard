#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk

class Application(tk.Frame):
    # ~ ALPHAS = ('abcde', 'fghij', 'klmno', 'pqrst', 'uvxy_')
    ALPHAS = ('ea_nrcv', 'jilphw', 'sudgk', 'tmbz', 'ofx', 'qy')
    BUTTONS = {
        'u' : 0,
        'i' : 1,
        'o' : 2,
        # ~ '4' : 0,
        # ~ '6' : 1,
        '6' : 0,
        '5' : 1,
        '4' : 2,
        }
    FONTSIZE=65
    NB_LETTER = 26
    
    def createWidgets(self):
        self.display = tk.Label(self, font=("Courier", self.FONTSIZE))
        self.display.pack({'side': 'top'})
        self.keyboard = tk.Text(self, font=("Courier", self.FONTSIZE))
        self.keyboard.pack({'side': 'bottom'})
        self.keyboard.insert('end', '\n'.join(('  '.join(i) for i in self.ALPHAS)))
        self.keyboard.config(state='disabled')
        self.standard_alpha(0)
        
    def __init__(self, master=None):
        super(Application, self).__init__(master)
        self.pack()
        self.createEvent()
        self.createWidgets()
        self.accum = ''
        self.series = None
        self.i_c, self.i_l = 0, 0
        self.last_key = 0

    def createEvent(self):
        self.master.bind("<Key>", self.key)
        self.master.bind("<ButtonRelease>", self.key)

    def standard_alpha(self, i_l=None, i_c=None):
        if i_c is None:
            self.keyboard.tag_delete('line')
        self.keyboard.tag_delete('char')
        if i_c is not None:
            i_l += 1
            self.keyboard.tag_add('char', "%d.%d" % (i_l, i_c * 3), "%d.%d" % (i_l, i_c * 3+3))
            self.keyboard.tag_config('char', foreground='yellow', background='red')
        elif i_l is not None:
            i_l += 1
            self.keyboard.tag_add('line', "%d.0" % i_l, "%d.45" % i_l)
            self.keyboard.tag_config('line', background='red')

    def key(self, event):
        if event.char in self.BUTTONS.keys() or event.keycode == 117 or event.num in [1,2,3]:
            if event.num in [1,2,3]:
                if event.num == 1:
                    i = 0
                elif event.num == 3:
                    i = 1
                elif event.num == 2:
                    i = 2
            elif event.keycode==117:
                i=2
            else:
                i = self.BUTTONS[event.char]
            
            if i == 2:
                if self.last_key == 1:
                    self.standard_alpha(self.i_l)
                    self.last_key = 0
                    self.i_c = 0
                elif self.last_key == 0:
                    self.accum = self.accum[:-1]
                    self.display['text'] = self.accum[-self.NB_LETTER:]
            elif i == 0:
                if self.last_key == 1:
                    self.accum += self.ALPHAS[self.i_l][self.i_c]
                    self.display['text'] = self.accum[-self.NB_LETTER:]
                    self.i_l, self.i_c = 0, 0
                else:
                    self.i_l += 1
                    self.i_l %= len(self.ALPHAS)
                self.last_key = 0
                self.standard_alpha(self.i_l)
            elif i == 1:
                if self.last_key == 0:
                    self.last_key = 1
                else:
                    self.i_c += 1
                    self.i_c %= len(self.ALPHAS[self.i_l])
                self.last_key = 1
                self.standard_alpha(self.i_l, self.i_c)

            
if __name__ == '__main__':
    app = Application()
    app.mainloop()
