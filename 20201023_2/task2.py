from itertools import islice

def elem3(iseq):
    return list(i for i in iseq if not i%2)

def elem(iseq):
    k = 0
    for i in iseq:
        l = list(islice(iseq, k, k+3))
        if len(l) == 3:
            yield from elem3(l)
        else:
            return
        k += 1

print(list(elem(eval(input()))))
