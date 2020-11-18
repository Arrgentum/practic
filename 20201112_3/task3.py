from decimal import Decimal

def S(x1,x2,x3,y1,y2,y3):
	a = (((x1-x2)**2)+((y1-y2)**2))**(1/2)
	b = (((x3-x2)**2)+((y3-y2)**2))**(1/2)
	c = (((x1-x3)**2)+((y1-y3)**2))**(1/2)
	p = (a+c+b)/2
	#print(a,c,b,p)
	Q = (p*(p-a)*(p-b)*(p-c))**(1/2)
	print(round(Q,3))


bool1 = True
while bool1:
	try:
		(x1, y1), (x2, y2), (x3, y3) = eval(input())
		if x1 == x2:
			if x2 == x3:
				print("Not a triangle")
			else:
				S(x1,x2,x3,y1,y2,y3)
				bool1 = not bool1
		else:
			k = (y2-y1)/(x2-x1)
			d = y1 - k*x1
			if k*x3 + d == y3:
				print("Not a triangle")
			else:
				S(x1,x2,x3,y1,y2,y3)
				bool1 = not bool1
	except:
		print("Ivalid input")