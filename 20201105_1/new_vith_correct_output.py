from re import *

a = input()

d = split(r",", a)
b1 = True
b2 = True
for i in d:
	dec1 = search(r"\s*[+-]?\d*\.?\d+", i)
	dec2 = search(r"\s*[+-]?\d+\.?\d*", i)
	sci1 = search(r"\s*[+-]?\d*\.?\d+[Ee][+-]?\d*", i)
	sci2 = search(r"\s*[+-]?\d+\.?\d*[Ee][+-]?\d*", i)
	#print(i)
	#if dec1:
	#	print("dec1 = ", dec1.group())
	#if dec2:
	#	print("dec2 = ", dec2.group())
	#if sci1:
	#	print("sci1 = ", sci1.group())
	#if sci2:
	#	print("sci2 = ", sci2.group())

	if (not dec1 or (dec1 and dec1.group() != i )) and (not dec2 or ( dec2 and dec2.group() != i )):
		b1 = False
	if (not sci1 or (sci1 and sci1.group() != i )) and (not sci2 or ( sci2 and sci2.group() != i )):	
		b2 = False

if b1 or b2:
    print("True")
else:
    print("False")

#if b2:
#	print("science numbers = Yes")
#else:
#	print("science numbers = No")
#if b1:
#	print("decimal numbers = Yes")
#else:
#	print("decimal numbers = No")
