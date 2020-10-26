from itertools import product

print( sorted( list(''.join(i) for i in product( *list("TOR" for i in range(int(input())))) if (''.join(i)).count("TOR") == 2 )))
