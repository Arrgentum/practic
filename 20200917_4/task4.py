import math

b = True
a, n = eval(input())
n1 = 1
while n1**n < a:
    n1 += 1
x =  0
while x <= n1 and b:
    y = 0
    while y <= n1 and b:
        z = 0
        while z <= n1 and b:
            if x**n + y**n + z**n == a:
                print(x,y,z)
                b = False
                break
            z += 1
        y += 1
    x += 1
if b:
    print("FAIL")

