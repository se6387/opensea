from operator import truediv


def printListWithFilter(list, filter):
    for l in list:
        if inFilter(l, filter):
            print('level : ', l)

def inFilter(l, filter):
    r = False
    for f in filter:
        if f in l:
            r = True
            break
    
    return r
