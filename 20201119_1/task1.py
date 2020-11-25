def deccount(fun):
	D = dict()
	def func(*args, **kwargs):
		nonlocal D
		if fun in D:
			D[fun] += 1
		else:
			D[fun] = 1
		print(D[fun])
		return fun(*args, **kwargs)
	return func

import sys
exec(sys.stdin.read())