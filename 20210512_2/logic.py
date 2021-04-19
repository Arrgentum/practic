"""Logical part of the application."""
import tkinter as tk


class Application(tk.Frame):
    """Sample tkinter application class."""

    def __init__(self, master=None, title="<application>", **kwargs):
        """Create root window with frame, tune weight and resize."""
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

    def check(self, txt, delt):
        """Entry validation."""
        return len(delt) <= 10 or len(delt) < len(txt)

    def ins_handler(self):
        """Insert button handler."""
        self.Ent.insert(tk.END, self.optvar.get())

    def show_handler(self):
        """Show button handler."""
        self.labvar.set(self.entvar.get())

