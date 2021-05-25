import unittest
def func(a,b,c):
    D = b**2 - 4 * a * c
    if D >= 0:
        return ((-b - D**(1/2)) / (2 * a), (-b + D**(1/2)) / (2 * a))
    return None

#def func(a, b, c):
#	d = b**2 - 4 * a * c
#	if d < 0:
#		return None
#	elif d == 0:
#		return (-b/(2 * a), -b/(2 * a))
#	else:
#		first = (-b + d**0.5) / (2 * a)
#		sec = (-b - d**0.5) / (2 * a)
#		return (min(first, sec), max(first, sec))

