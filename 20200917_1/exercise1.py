a = int(input())

if a%50 == 0:
    x = "+"
else:
    x = "-"
if a%25 == 0 and a%2 == 1:
    y = "+"
else:
    y = "-"
if  a%8 == 0:
    z = "+"
else:
    z = "-"
print("A"+x+" B"+y+" C"+z)
