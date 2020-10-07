a = list()
d = list()
c = input()
while bool(c):
    c = eval(c)
    b = True
    for i in d:
        if c[0] < i[0] and c[1] < i[1]:
            b = False
        elif c[0] > i[0] and c[1] > i[1]:
            for j in range(a.count(i)):
                a.remove(i)
    if b or len(a) == 0:
        a.append(c)
    d.append(c)
    c = input()
print(a)
