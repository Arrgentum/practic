def Bisect(a ,d):
    def checksort(b):
        if len(b) > 0:
            z = b[0]
            for i in b:
                if z > i:
                    return False
                z = i
            return True
        else:
            return False
    
    def check(a, b):
        if len(b)==1:
            if a==b[0]:
                return True
            else:
                return False
        else:
            if b[len(b)//2] < a:
                if type(b) == str:
                    c = b[len(b)//2 : len(b)]
                    return check(a, c)
                elif type(b) == tuple:
                    c = list()
                    for i in range(len(b)//2+1, len(b)):
                        c.append(b[i])
                    c = tuple(c)
                    return check(a,c)
                elif type(b) == list:
                    c = list()
                    for i in range(len(b)//2+1, len(b)):
                        c.append(b[i])
                    return check(a,c)
            elif b[len(b)//2] > a:
                if type(b) == str:
                    c = b[0 : len(b)//2]
                    return check(a,c)
                elif type(b) == tuple:
                    c = list()
                    for i in range(len(b)//2):
                        c.append(b[i])
                    c = tuple(c)
                    return check(a,c)
                elif type(b) == list:
                    c = list()
                    while i < range(len(b)//2):
                        c.append(b[i])
                    return check(a,c)
            else: 
                return True
    if checksort(d):
        return check(a,d)
    else:
        return False
