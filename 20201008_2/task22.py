def sum(a,s):
    c = 0
    for i in range(len(a)):
        c += (s**(len(a)-i)) * a[i]
    return c

s,w,*l = eval(input())
a = sum(list(l[i] for i in range(1, l[0]+2)) , s)
b = sum(list(l[i] for i in range(l[0]+3, len(l))) , s)
if (b == 0) or (a/b != w):
    print("False")
else:
    print("True")
