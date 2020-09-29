a = list(eval(input()))
b = list()
for i in range(0,100):
    for j in a:
        if ((j%100)**2)%100 == i:
            b.append(j)
print(b)

