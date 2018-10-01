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

'''
Quiz: Recognize Identity Matrix
    * If you want to write code that will run on both Python 2 and Python 3, use range() as the xrange function is deprecated in Python 3.
'''
def is_identity_matrix(m):
    n = len(m)
    i = 0
    for e in m:
        if len(m) != len(e):
            return False
    while i < n:
        j = 0
        while j < n:
            if m[i][j] != m[j][i]:
                return False
            elif i == j and m[i][j] != 1:
                return False
            elif i != j and m[i][j] != 0:
                return False
            j = j + 1
        i = i + 1
    return True

# Alternative solution #1
def is_identity_matrix(matrix):
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            return False
    for i in xrange(n):
        for j in xrange(n):
            if i == j and matrix[i][j] != 1:
                return False
            elif i != j and matrix[i][j] != 0:
                return False
    return True

# Alternative solution #2
# '\' allows a line of code to be broken into two lines
def is_identity_matrix(matrix):
    n = len(matrix) # the number of rows
    return all(len(row) == n for row in matrix) and \ 
           all(matrix[x][y] == (1 if x == y else 0)
               for x in xrange(n) for y in xrange(n))

# Alternative solution #3
def is_identity_matrix(m):
    return m == [[int(x==y) for y in xrange(len(m))]
                            for x in xrange(len(m))]


'''
Quiz: Numbers in Lists
'''
def numbers_in_lists(string):
    result = []
    while string:
        result.append(int(string[0]))
        sub = []
        i = 1
        while i < len(string):
            if int(string[i]) > int(string[0]):
                break
            else:
                sub.append(int(string[i]))
                i += 1
        if sub:
            result.append(sub)
        string = string[i:]
    return result

'''
Quiz: Frequency Analysis
'''
def freq_analysis(msg):
    msg_list =[]
    for e in msg:
        msg_list.append(e)
    freq_list=[]
    list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    i=0
    while i<len(list):
        count=0
        j=0
        while j<len(msg):
            if msg_list[j] == list[i]:
                count = count+1
            j=j+1 
        freq_list.append(float(count)/len(msg))
        i=i+1    
       
    return freq_list

# Alterative solution
# Much more efficient than the first solution
def freq_analysis(message):
    num_list = [0] * 26
    for letter in message:
        offset = ord(letter) - ord('a') # one of 0, 1, ..., 25
        num_list[ offset ] += 1
    n = float(len(message))
    return [ i / n for i in num_list ]