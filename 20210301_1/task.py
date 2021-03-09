import tkinter as tk

class Application(tk.Frame):
	def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
    	self.itemLabel = tk.Label(self, textvariable = self.var)
    	self.itemLabel.grid(row = 0, column = 2)
        self.nextItem.grid(row = 0, column = 3)
        self.exitButton.grid(row = 0, column = 4)



app = Application()
app.master.title('Menu')
app.mainloop()