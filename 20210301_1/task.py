import tkinter as tk

class Application(tk.Frame):
	def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
    	self.exitButton = tk.Button(self, text='Exit', command=self.exit)
    	self.itemLabel = tk.Label(self, textvariable = self.var)

    	self.optionMenu = tk.OptionMenu(self, self.variable, *self.optionList)
    	self.optionMenu.grid(row = 0, column = 1)
    	self.itemLabel.grid(row = 0, column = 2)
        self.nextItem.grid(row = 0, column = 3)
        self.exitButton.grid(row = 0, column = 4)


    """Exit buttom"""
    def exit(self):
        self.quit()



app = Application()
app.master.title('Menu')
app.mainloop()
