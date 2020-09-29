x = input()
s2 = set()
s1 = set()
l = list()
while bool(x):
    l.append(x)
    x = set(x)
    for i in x:
        if i in s2:
            s2.remove(i)
    y = set(i for i in x if i not in s1)
    s2.update(set(i for i in x if i not in s1))
    s1.update(x)
    x = input()
for i in l:
    if set(i) <= s2:
        print(i)
