import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None, title="<application>", **kwargs):
        super().__init__(master, **kwargs)
        self.master.title(title)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.grid(sticky="NEW")
        self.create_widgets()
        for column in range(self.grid_size()[0]):
            self.columnconfigure(column, weight=1)
        for row in range(self.grid_size()[1]):
            self.rowconfigure(row, weight=1)

    def create_widgets(self):
        pass

class App(Application):
    def create_widgets(self):
        super().create_widgets()
        self.Text = tk.Text(self, padx=10, pady=10)
        self.string = [""]
        self.figure = ["oval", "rectangle", "line"]
        self.Canvas = tk.Canvas(self)
        self.Run = tk.Button(self, text="Run", command=self.run_handler)
        self.Clear = tk.Button(self, text="Clear", command=self.clear)
        self.Quit = tk.Button(self, text="Quit", command=self.master.quit)
        self.HintText = tk.StringVar()
        self.Hint = tk.Label(self, textvariable=self.HintText)
        self.Text.grid(row=0, column=0)
        self.Text.bind("<KeyPress>", self.text_input)
        self.Text.bind("<Motion>", self.mouse)
        self.Text.tag_config("no", foreground="red")
        self.Text.tag_config("yes", foreground="green")
        self.Canvas.grid(row=0, column=1, sticky="NEWS")
        self.Run.grid(row=2, column=0)
        self.Clear.grid(row=2, column=1)
        self.Quit.grid(row=3, column=0)
        self.Hint.grid(row=1, column=1)

    def text_input(self, event):
        self.string = self.Text.get("1.0", tk.END).split("\n")
        for line_num, line in enumerate(self.string):
            words = line.split(" ")
            if line.startswith("#") or words[0] in self.figure:
                self.tag_setter("no", "yes", line_num)
            else:
                self.tag_setter("yes", "no", line_num)

    def run_handler(self):
        for figure in self.Canvas.find_all():
            self.Canvas.delete(figure)
        self.figure_input()

    def clear(self):
        for figure in self.Canvas.find_all():
            self.Canvas.delete(figure)

    def tag_setter(self, tag_rem, tag_set, ind):
        self.Text.tag_remove(tag_rem, str(ind + 1) + ".0", str(ind + 1) + ".0 lineend")
        self.Text.tag_add(tag_set, str(ind + 1) + ".0", str(ind + 1) + ".0 lineend")

    def figure_input(self):
        self.string = self.Text.get("1.0", tk.END).split("\n")
        for line_num, line in enumerate(self.string):
            words = line.split(" ")
            if words[0] in self.figure:
                try:
                    eval(f"self.Canvas.create_{words[0]}({','.join(words[1:])})")
                    self.tag_setter("no", "yes", line_num)
                except:
                    self.tag_setter("yes", "no", line_num)
            elif line.startswith("#"):
                self.tag_setter("no", "yes", line_num)
            else:
                self.tag_setter("yes", "no", line_num)

    def mouse(self, event):
        coordinates = self.Text.index(tk.CURRENT).split('.')
        point, words = int(coordinates[0]), [""]
        if self.string[0] != '':
            words = self.string[point-1].split(" ")
        if words[0] in self.figure:
            if words[0] == "oval" or words[0] == "rectangle":
                self.HintText.set("Draw " + words[0] + ": " + words[0] + " x0 y0 x1 y1 outline='color' ""fill='color' width='width'")
            elif words[0] == "line":
                self.HintText.set("Draw line: line x0 y0 x1 y1 width='width' fill='color'")
        elif words[0].startswith("#"):
            self.HintText.set("Comment")
        elif self.string[0] != '' and self.string[point-1].isspace() is True or words[0] == '':
            self.HintText.set("Empty string")
        else:
            self.HintText.set("Not CCL string")

app = App(title = "Figure drawer from CCL")
app.mainloop()