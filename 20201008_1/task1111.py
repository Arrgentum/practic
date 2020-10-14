from math import *

a = input()
f = lambda x: eval(a)
print("Введите диапозон Х")
X = eval(input())
print("Введите диапозон У")
Y = eval(input())
x = 80 / (X[1] - X[0])
y = 20 / (Y[1] - Y[0])
K = []
#L = list((i , round(f(i/x)*y) ) for i  in range(int(X[0]*x), int(X[1]*x+1)))
L = []
for i in range(int(X[0]*x), int(X[1]*x+1)):
    try:
        L.append((i, round(f(i/x)*y)))
    except ZeroDivisionError:
        j = float(str(i) + ".0001")
        K.append((i, round(f(j/x)*y)))
L1 = list((0, i) for i in range(int(Y[0]*y), int(Y[1]*y+1)))
L2 = list((i, 0) for i in range(int(X[0]*x), int(X[1]*x+2)))

for j in reversed(range(int(Y[0]*y), int(Y[1]*y))):
    s = ""
    for i in range(int(X[0]*x), int(X[1]*x)):
        if (i,j) in L:
            s += "*"
        elif (i, j) in K:
            s += "."
        elif (i,j) in L1:
            s += "|"
        elif (i,j) in L2:
            s += "-"
        else:
            s += " "
    print(s)
