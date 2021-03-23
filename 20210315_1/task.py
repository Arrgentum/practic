import tkinter as tk
from itertools import product
from re import match

class Application(tk.Frame):
    def __init__(self, master=None, title="<application>", **kwargs):
        super().__init__(master, **kwargs)
        self.master.title(title)
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
    str = ""
    def create_widgets(self):
        alpha = self.register(self.alpha)
        self.S = tk.StringVar()
        self.E = tk.Entry(self, textvariable=self.S,
                validate='all', validatecommand=(alpha, '%P'))
        self.E.grid(columnspan=2)
        self.L = tk.Label(self, text="Reals only")
        self.L.grid(row=1, column=0)
        self.Q = tk.Button(self, text="Quit", command=self.exit)
        self.Q.grid(row=1, column=1)

    def alpha(self, txt):
        #print(f"{txt}")
        if bool(match(r"[+-]?((\d+)?([.]\d*)?|(\d*[.])?\d+)([Ee][+-]?\d+)?$",txt)):
            self.str = txt
            return True
        return False

    def exit(self):
        print(self.str)
        self.master.quit()

app = App(title="Sample application")
app.mainloop()
