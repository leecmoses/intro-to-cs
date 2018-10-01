#########
# Notes #
#########
'''
Quiz: Antisymmetric Square
'''
def antisymmetric(A):
    n = len(A)
    i = 0
    for e in A:
        if len(A) != len(e):
            return False
    while i < n:
        j = 0
        while j < n:
            if A[i][j] != -A[j][i]:
                return False
            j = j + 1
        i = i + 1
    return True