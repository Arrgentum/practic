b = False
for i in reversed(list(enumerate(input()))):
    if i[1] in "ABC":
        if i[1] == "B":
            print(a)
        b = not b
    elif not b and i[1] in "12345":
        a = list(i)
        b = not b 
