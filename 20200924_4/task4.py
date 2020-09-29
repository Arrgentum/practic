b = False
for i in reversed(list(enumerate(input()))):
    if i[1] ==  "B":
        if not b:
            b = not b
        print(a)
    elif not b and i[1] in "12345":
            a = list(i)
