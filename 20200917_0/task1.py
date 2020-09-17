a, b, c = eval(input())

if a+b>c and a+c>b and b+c>a and all((a>0, b>0, c>0)):
    print("yes")
else:
    print("no")
