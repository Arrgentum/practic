from . import solve, fig
import gettext
import os

gettext.install("solve", os.path.dirname(__file__), names=("ngettext",))


a, b = map(float, input(_("Input a b: ")).split())
print("\n", fig(solve(a, b)))

