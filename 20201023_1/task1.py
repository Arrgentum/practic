def Fib(m,n):
    a, b = 1,1
    for j in range(3, n+1):
        a, b = b, a + b
        if j >= m:
            yield b

m, n = eval(input())
print(list(Fib(m, n)))
