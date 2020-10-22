import random

string1 = "УЁЕУЫАОЭЯИЮ"
string2 = ""
for i in range(ord("А"), ord("Я")+1):
    if chr(i) not in string1 and chr(i) not in "ЬЪ":
        string2 = string2 + chr(i)
output_string = ""
a = int(input())
i = 0
while i < a:
    j = random.randint(1,3)
    if j == 1:
        output_string = output_string + string1[random.randint(0,9)]
        i += 1
    elif j == 2:
        output_string = output_string + string1[random.randint(0,9)] + string2[random.randint(0, len(string2)-1)] 
        i += 2
    else:
        output_string = output_string + string2[random.randint(0, len(string2)-1)] + string1[random.randint(0, 9)]
        i += 2
print(output_string)
