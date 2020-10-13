a,b = eval(input())
d = 6+4*len(str(a)) #block length
if len(str(a))*2 == len(str(a*a)):
    d += 1
c = 0 
f = b//(d+1) #number of blocks in line
c = a//f #number of blocks in height
k = a%f #number of block in last line
if a%f > 0:
    c += 1
delimeter_string = "="
delimeter_string *= b
input_string = " {} * {} = {}"
output_string1 = "{:{d}} |"
output_string2 = "{:{d}} |"
output_string1 = output_string1*(f-1) + "{:^{d}}"
output_string2 = output_string2*(k-1) + "{:^{d}}"
i = 0
print(c, d, k, f)
while i < c:
    print(delimeter_string)
    j = 1
    if i<c-1 or k == 0:
        while j <= a:
            p = list(input_string.format(f*i+n, j, (f*i+n)*j) for n in range(1, f+1))
            print(output_string1.format(*p, d = d))
            j += 1
    else:
        while j <= a:
            p = list(input_string.format(f*i+n, j, (f*i+n)*j) for n in range(1, k+1))
            print(output_string2.format(*p, d = d ))
            j += 1
    i += 1
print(delimeter_string)
