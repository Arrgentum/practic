import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.timeButton.grid()
        self.quitButton.grid(row=0, column=1)
        self.timeLabel.grid(columnspan=2)


app.master.title('Sample timer application')
app = Application()
app.mainloop()
