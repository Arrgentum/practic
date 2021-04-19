"""Program."""
import tkinter as tk


class Application(tk.Frame):
    """Sample tkinter application class."""

    def __init__(self, master=None, title="<application>", **kwargs):
        """task."""
        super().__init__(master, **kwargs)
        self.master.title(title)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.grid(sticky="NEWS")
        self.create_widgets()
        for column in range(self.grid_size()[0]):
            self.columnconfigure(column, weight=1)
        for row in range(self.grid_size()[1]):
            self.rowconfigure(row, weight=1)

    def create_widgets(self):
        """Create all the widgets."""


class App(Application):
    """Application function."""

    def create_widgets(self):
        """Create widgets."""
        super().create_widgets()
        text = self.register(self.text)
        self.S = tk.StringVar()
        self.E = tk.Entry(
                self, textvariable=self.S, validate='all', validatecommand=(text, '%s', '%S', '%P'))
        self.lab = tk.StringVar()
        self.lab.set('Default')
        self.Insert = tk.Button(self, text="Insert", command=self.insert)
        self.Show = tk.Button(self, text="Show", command=self.show)
        self.Printer = tk.Label(self, textvariable=self.lab, width=10)
        self.optionList = ("One", "Two", "Three")
        self.ItemVar = tk.StringVar()
        self.ItemVar.set(self.optionList[0])
        self.OptionMenu = tk.OptionMenu(self, self.ItemVar, *self.optionList)

        self.OptionMenu.grid(row=2, column=0, sticky='W')
        self.Insert.grid(row=1, column=0, sticky='W')
        self.E.grid(row=0, column=0, columnspan=2, sticky='WE')
        self.Printer.grid(row=2, column=1, sticky='W')
        self.Show.grid(row=1, column=1, sticky='W')

        self.Printer.bind('<Enter>', self.hi)
        self.Printer.bind('<Leave>', self.bye)

    def insert(self):
        """Insert the entry."""
        if len(self.S.get()) + len(self.ItemVar.get()) <= 10:
            self.E.insert(tk.END, self.ItemVar.get())

    def text(self, txt, ch, deletion):
        """Control the text-entry."""
        if len(txt) < 10 or len(deletion) < len(txt):
            return ch.isprintable()
        else:
            return False

    def show(self):
        """Show Button."""
        self.lab.set(self.S.get())

    def hi(self, event):
        """Catched mouse."""
        self.lab.set('Hi Mouse')

    def bye(self, event):
        """Uncatched mouse."""
        self.lab.set('Bye Mouse')


def main():
    """Wrap it."""
    app = App(title="Sample application")
    app.mainloop()


if __name__ == "__main__":
    main()

