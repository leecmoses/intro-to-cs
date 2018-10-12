#############
#   Notes   #
# Lesson 28 #
#############
'''
Quiz: Stirling and Bell
'''
def stirling(n, k):
    if n < k:
        return 0
    if n == k or k == 1:
        return 1
    return k*stirling(n-1, k) + stirling(n-1, k-1)

def bell(n):
    total = 0
    for k in range(1, n+1):
        total = total + stirling(n,k)
    return total

'''
Quiz: Combating Link Spam
'''


'''
Quiz: Elementary Cellular Automation
'''
