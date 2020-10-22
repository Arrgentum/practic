import sys
import random

# создание строк и словарей

allstr = list(chr(i) for i in range(ord("а"), ord("я")))
string1 = "ёуеыаоэяию"
separators = "',.!`;?:\-_()[]{}" + "\""
dictionary = {i : {j : 0 for j in allstr if (((i in string1) and (j not in string1)) or ((i not in string1) and (j in string1)))} for i in allstr}
for i in dictionary:
    (dictionary[i])["add"] = 0

#чтение книги и заполнений словарей

sum1 = 0
while True:
    try:
        a = input().lower()
    except EOFError:
        break
    for i in separators:
        a.format(i, " ")
    b = a.split()
    for k in b:
        j = ""
        for i in k:
            if j in dictionary and i in dictionary[j]:
                dictionary[j][i] += 1
                dictionary[j]["add"] += 1
                sum1 += 1
            j = i

#выбор первого рандомного слога

if len(sys.argv) > 2:
    random.seed(sys.argv[2])
sum2 = 0
rand = random.randint(1, sum1)
for i in dictionary:
    if sum2 + dictionary[i]["add"] > rand:
        for j in dictionary[i]:
            sum2 += dictionary[i][j]
            if sum2 > rand:
                cur = j
                break
        break
    else:
        sum2 += dictionary[i]["add"]
j = cur
output = i + j

#выбор остальных рандомных слогов

k = 2
while k < int(sys.argv[1]):
    rand = random.randint(1, dictionary[j]["add"])
    sum2 = 0
    for i in dictionary[j]:
        sum2 += (dictionary[j])[i]
        if sum2 > rand:
            break
    j = i
    k += 1
    output += i
print(output)
