###########
## Notes ##
###########

'''
Quiz: Stamps
'''
def stamps(num):
    return num / 5, (n % 5) / 2, (n % 5) % 2

'''
Quiz: Range of a Set
'''
def set_range(a, b, c):
    smallest = min(a, b, c)
    biggest = max(a, b, c)
    return biggest - smallest

# Alternatively
def set_range(a, b, c):
    a, b, c = sorted([a, b, c])
    return c - a