import tkinter as tk
import re
"""
    This is module.
"""

class Application(tk.Frame):
    def __init__(self, master=None, title="<application>", **kwargs):
        """Create root window with frame, tune weight and resize"""
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
        """Create all the widgets"""


class App(Application):
    def create_widgets(self):
        """Create widgets"""
        self.ES = tk.StringVar()
        self.OS = tk.StringVar()
        self.LS = tk.StringVar()
        self.LS.set("Default")

        validate_word = self.register(self.check_word)
        self.checker = re.compile(r"^\w{0,10}$")
        self.E = tk.Entry(self, textvariable=self.ES, validate='key', validatecommand=(validate_word, "%P"))

        self.L = tk.Label(self, textvariable=self.LS)
        self.L.bind('<Enter>', lambda event: self.LS.set("Hi Mouse"))
        self.L.bind('<Leave>', lambda event: self.LS.set("Bye Mouse"))

        self.OList = ("One", "Two", "Three")
        self.OS.set(self.OList[0])
        self.OM = tk.OptionMenu(self, self.OS, *self.OList)
        self.I = tk.Button(self, text="Insert", command=lambda: self.E.insert(tk.END, self.OS.get()))
        self.S = tk.Button(self, text="Show", command=lambda : self.LS.set(self.ES.get()))
        self.Q = tk.Button(self, text="Quit", command=self.master.quit)
        self.set_grid()

    def set_grid(self):
        """grids"""
        self.E.grid(row=0, columnspan=3, sticky="NEWS")
        self.OM.grid(row=1, column=0, sticky="NEWS")
        self.L.grid(row=1, column=1, columnspan=2, sticky="NEWS")
        self.Q.grid(row=2, column=2, sticky="NEWS")
        self.I.grid(row=2, column=0, sticky="NEWS")
        self.S.grid(row=2, column=1, sticky="NEWS")

    def check_word(self, word):
        """check"""
        return self.checker.fullmatch(word) is not None


app = App(title="Sample application")
app.mainloop()
