def Calc(t, s, u):
    def newf1(x):
        return eval(t )

    def newf2(x):
        return eval(s)

    def newf3(x,y):
        return eval(u)

    def func(x):
        return newf3(newf1(x) , newf2(x))

    return func
