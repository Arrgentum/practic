s=0
while s<=21:
    a = int(input())
    s = s+a
    if a<=0:
        print(s)
        break
else:
    if s>21:
        print(0)

