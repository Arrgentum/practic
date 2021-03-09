import tkinter as tk

class Application(tk.Frame):
	def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
    	self.exitButton = tk.Button(self, text='Exit', command=self.exit)
    	self.nextItemButton = tk.Button(self, text='Next Item', command=self.nextItem)
    	self.itemLabel = tk.Label(self, textvariable = self.variable)
    	self.optionList = ('One', 'Two', 'Three')
    	self.variable = tk.StringVar()
        self.variable.set(self.optionList[0])
    	self.optionMenu = tk.OptionMenu(self, self.variable, *self.optionList)
    	self.optionMenu.grid(row = 0, column = 1)
    	self.itemLabel.grid(row = 0, column = 2)
        self.nextItemButton.grid(row = 0, column = 3)
        self.exitButton.grid(row = 0, column = 4)


    """Exit buttom"""
    def exit(self):
        self.quit()

    """Next item button"""
    def nextItem(self):
        b = self.optionList.index(self.variable.get())
        if b == len(self.optionList) - 1:
            self.variable.set(self.optionList[0])
        else:
            self.variable.set(self.optionList[b+1])


app = Application()
app.master.title('Menu')
app.mainloop()
