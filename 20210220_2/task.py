import tkinter as tk
from subprocess import run

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.createWidgets()


    def showdir(self):
        self.result.set(run("dir", capture_output=True).stdout)
    
    def showdate(self):
        self.result.set(run("date", capture_output=True).stdout)
    
    def showgit(self):
        self.result.set(run("git", capture_output=True).stdout)


    def createWidgets(self):
        self.result = tk.StringVar()
        self.result.set('Select')
        self.dir_button = tk.Button(self, text="dir", command=self.showdir)
        self.date_button = tk.Button(self, text="date", command=self.showdate)
        self.git_button = tk.Button(self, text="git", command=self.showgit)
        self.quit_button = tk.Button(self, text='Quit', command=self.quit)
        
        self.but_Label = tk.Label(self, textvariable = self.result)
        
        self.dir_button.grid(row = 0, column = 1)
        self.date_button.grid(row = 0, column = 2)
        self.git_button.grid(row = 0, column = 3)
        self.quit_button.grid(row = 0, column = 4)

        self.but_Label.grid(row = 1, columnspan = 4)


app = Application()
app.master.title('dir/date/git')
app.mainloop()