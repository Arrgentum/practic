class nestr(str):
	def __neg__(self):
		return nestr("".join(reversed(self)))

	def __add__(self, other):
		return nestr("".join(str(self)+str(other)))
	
	def __mul__(self, other):
		return nestr("".join(str(self) * int(other)))

print(eval(input()))
