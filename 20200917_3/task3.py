for i in range(3,7):
    for j in range(3,7):
        a = i*j
        if a%10 + a//10 == 6:
            print(":=)", end = ' ')
        else:
            print(i*j, end = ' ')
    print()
