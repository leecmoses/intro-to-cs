###########
## Notes ##
###########

'''
Quiz: Median
'''
def median(a,b,c):
    big = biggest(a,b,c)
    if big == a:
        return bigger(b,c)
    if big == b:
        return bigger(a,c)
    else:
        return bigger(a,b)

'''
Quiz: Blastoff
'''
def countdown(n):
    while n > 0:
        print n
        n = n - 1
    print 'Blastoff!'

'''
Quiz: Finish
* Loop 3 is a Collatz Conjecture!
'''

'''
Quiz: Find Last

'''

def find_last(s,t):
    last_pos = -1
    while True:
        pos = s.find(t, last_pos + 1)
        if pos == -1:
            return last_pos
        else:
            last_pos = pos