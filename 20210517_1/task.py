import pyfiglet 

gettext.install('task', os.path.dirname(__file__), names=("ngettest",))

a, b = map(int, input().split()) 

def solve(a,b):
    if a != 0:
        return -b/a

    if a == 0:
        return None

res = solve(a,b)
f = pyfiglet.Figlet()
print( f.renderText("NO ROOTS") if res is None else f.renderText("Root: {}".format(res)) )

