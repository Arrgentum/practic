import tkinter as tk
from MVC import Model, View, Control


class AppView(View):
    '''Square solve.'''

    def createWidgets(self):
        '''Solver layout.'''
        self.aString = tk.StringVar()
        self.aEntry = tk.Entry(self, textvariable=self.aString)
        self.bString = tk.StringVar()
        self.bEntry = tk.Entry(self, textvariable=self.bString)
        self.cString = tk.StringVar()
        self.cEntry = tk.Entry(self, textvariable=self.cString)
        self.aLabel = tk.Label(self, text="a = ")
        self.bLabel = tk.Label(self, text="b = ")
        self.cLabel = tk.Label(self, text="c = ")
        self.mainLabel = tk.Label(self, text="a * x^2 + b * x^2 + c = 0")
        self.resultString = tk.Label(self)
        self.go = tk.Button(self, text="Вычислить")
        self.Q = tk.Button(self, text="Выход", command=self.master.quit)

        self.mainLabel.grid(sticky="NEWS", row=0, columnspan=6)
        self.aLabel.grid(sticky="NEWS", row=1, column=0)
        self.bLabel.grid(sticky="NEWS", row=1, column=2)
        self.cLabel.grid(sticky="NEWS", row=1, column=4)
        self.aEntry.grid(sticky="NEWS", row=1, column=1)
        self.bEntry.grid(sticky="NEWS", row=1, column=3)
        self.cEntry.grid(sticky="NEWS", row=1, column=5)
        self.resultString.grid(sticky="NEWS", row=2, columnspan=6)
        self.go.grid(sticky="NEWS", row=3, columnspan=6)
        self.Q.grid(sticky="NEWS", row=0, column=6, rowspan=4)


    def assingbindings(self):
        """Initiate control events if calculate - button pressed."""
        self.go["command"] = self.control.calculate

class AppControl(Control):
    """Simple control: no view → model translation."""

    def calculate(self):
        """Need calculate answer."""
        self.model.calculate()

    def setup(self):
        """Ask model print welcom line."""
        self.model.initialstate()


class AppModel(Model):
    """Square app logic"""

    def initialstate(self):
        self.view.resultString["text"] = "Enter all coefficients"

    def calculate(self):
        '''Get coefficient from input.'''
        try:
            ''' Wrong input '''
            a = float(self.view.aString.get())
            b = float(self.view.bString.get())
            c = float(self.view.cString.get())
            result = self.calculateresult(a, b, c)
        except Exception as E:
            result = f"{E}"
            if result[-2:] == "''":
                result = "Enter all coefficients"
        self.view.resultString["text"] = result

    def calculateresult(self, a, b, c):
        '''Calculate answer.'''
        if not(a) and not(b) and not(c):
            return "∞"
        if not(a) and not(b):
            return "∅"
        if not(a):
            return -c / b
        else:
            D = b**2 - 4 * a * c
            if D > 0:
                return ((-b - D**(1/2)) / (2 * a), (-b + D**(1/2)) / (2 * a))
            if D == 0:
                return -b / (2 * a)
            if D < 0:
                return "∅"


def main():
    """Call main application."""
    view = AppView(title="Square solver")
    model = AppModel(view)
    control = AppControl(model)
    model(control)


if __name__ == "__main__": # pragma: no cover
    main()

