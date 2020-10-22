list1 = list()
j = ""
for i in input().lower():
    if j != "" and (j,i) not in list1 and i.isalpha() and j.isalpha():
        list1.append( (j,i) )
    j = i
print(len(list1))
