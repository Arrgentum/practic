import tkinter as tk

class Application(tk.Frame):
	def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
    	self.exitButton = tk.Button(self, text='Exit', command=self.exit)
    	self.itemLabel = tk.Label(self, textvariable = self.var)
    	self.itemLabel.grid(row = 0, column = 2)
        self.nextItem.grid(row = 0, column = 3)
        self.exitButton.grid(row = 0, column = 4)

    
    def exit(self):
        """Handler for the exit button that closes the application window"""
        self.quit()



app = Application()
app.master.title('Menu')
app.mainloop()
