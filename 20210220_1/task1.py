import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid()

<<<<<<< HEAD
app.master.title('Sample timer application')
=======
app = Application()
app.master.title('Sample application')
>>>>>>> 237cf325ddc86faf304b8817261861cd4f229f53
app.mainloop()
