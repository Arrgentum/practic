import tkinter as tk

class View(tk.Frame):
    '''
    Sample tkinter View class.

    :param master: master window (tkinter root if None)
    :param title: application window title
    '''
    
    def __init__(self, master=None, title="<application>", control=None, **kwargs):
        '''Create root window with frame, tune weight and resize.'''
        self.control = control
        super().__init__(master, ** kwargs)
        if not master: # pragma: no cover
            self.master.title(title)
            self.master.columnconfigure(0, weight=1)
            self.master.rowconfigure(0, weight=1)
            self.grid(sticky="NEWS")
        self.createWidgets()
        for column in range(self.grid_size()[0]):
            self.columnconfigure(column, weight=1)
        for row in range(self.grid_size()[1]):
            self.rowconfigure(row, weight=1)

    def createWidgets(self):
        '''Create all the widgets.'''

    def assingbindings(self):
        """Assign controller bindings."""
        
    def __call__(self, control=None):
        '''Start an application.'''
        self.control = control
        self.assingbindings()
        self.mainloop()
        del self.control
        
class Model:
    '''
    Trivial program logic.

    :param view: View part of MVC framework
    '''

    def __init__(self, view):
        '''Set up view instance field.'''
        self.view = view

    def __call__(self, control=None):
        '''
        Initialize view instance.

        :param control: Control part of MVC framework
        '''
        if control: # pragma: no cover
            control.setup()
        self.view(control)

class Control:
    """
    Trivial program controller.

    :param model: Model part of MVC framework
    """

    def __init__(self, model):
        """Set up model instance field."""
        self.model = model

    def setup(self):
        """Command Model to set up stuff."""

