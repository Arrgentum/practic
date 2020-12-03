import sys


data = sys.stdin.read()
print(data.encode("latin", errors = "replace").decode("CP1251" , errors = "replace"))
