#########
# Notes #
#########
'''
Quiz: Symmetric Square
'''
def symmetric(p):
    n = len(p)
    i = 0
    for e in p:
        if len(p) != len(e):
            return False
    while i < n:
        j = 0
        while j < n:
            if p[i][j] != p[j][i]:
                return False
            j = j + 1
        i = i + 1
    return True

'''
Quiz: Mean of a List
'''
def list_mean(p):
    sum = 0.0
    number = len(p)
    for i in p:
        sum = sum + i
    return sum / number