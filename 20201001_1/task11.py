def SUB(x,y):
    if type(x) != type(y):
        print("Different type")
        return ()
    elif type(x) == int or type(x) == float or type(x) == set:
        return x - y
    else:
        if type(x) == str:
            string = str()
            for i in x:
                if i not in y:
                    string += i
            return string
        elif type(x) == list:
            L = list(i for i in x if i not in y)  
            return L
        elif type(x) == tuple:
            L = tuple(i for i in x if i not in y)
            return L
