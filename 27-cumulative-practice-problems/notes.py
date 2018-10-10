#############
#   Notes   #
# Lesson 27 #
#############
'''
Quiz: Pick One
'''
def pick-one(boolean, true_response, false_response):
    if boolean:
        return true_response
    else:
        return false_response

'''
Quiz: Triangular Numbers
'''
def triangular(n):
    sum = 0
    i = 0
    while i < n:
        i += 1
        sum += i
    return sum

# Alternative solution
def triangular(n):
    number = 0
    for i in range(1, n+1):
        number += i
    return number

'''
Quiz: Remove Tags

Plan
    1) Remove tags and replace with a space.
    2) Use split() to turn string into a list.
'''
def remove_tags(string):
    start = string.find('<')
    while start != -1:
        end = string.find('>', start)
        string = string[:start] + ' ' + string[end + 1:]
        start = string.find('<')
    return string.split()
