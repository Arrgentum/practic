'''
Tkinter skeleton app
'''
import tkinter as tk
from itertools import product
import re
import gettext

gettext.install('task', localedir='po', names=("ngettext",))

class Application(tk.Frame):
    '''Sample tkinter application class'''

    def __init__(self, master=None, title="<application>", **kwargs):
        '''Create root window with frame, tune weight and resize'''
        super().__init__(master, **kwargs)
        self.master.title(title)
        self.check = False
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.grid(sticky="NEWS")
        self.create_widgets()
        for column in range(self.grid_size()[0]):
            for row in range(self.grid_size()[1]):
                self.columnconfigure(column, weight=1)
            self.rowconfigure(row, weight=1)

    def create_widgets(self):
        '''Create all the widgets'''

class App(Application):
    def create_widgets(self):
        self.num = 0
        self.N = tk.Button(self, text=_('0 times'),  command=self.new_num)
        self.N.grid(row=1, column=1)

    def new_num(self):
        self.num += 1
        self.N["text"] = ngettext("%d time clicked", "%d times clicked", self.num)%(self.num)


app = App(title="Numbers application")
app.mainloop()
