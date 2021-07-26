import pyfiglet
import locale
import gettext
import os

gettext.install("solve", os.path.dirname(__file__), names=("ngettext",))


def solve(a: float, b: float):
    if a == 0:
        return None
    return -b / a


def fig(res) -> str:
    if locale.getlocale()[0] == "ru_RU":
        f = pyfiglet.Figlet(font="graceful") 
    else:
        f = pyfiglet.Figlet()
    if res is None:
        return f.renderText(_("NO ROOTS"))
    return f.renderText(_("Root: %.5f") % (res,))

