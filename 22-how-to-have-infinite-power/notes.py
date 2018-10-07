#############
#   Notes   #
# Lesson 22 #
#############
'''
Recursive Definitions
    Two parts:
    1. Base case - a starting point (Not defined in terms of itself)
        * Smallest input - already know the answer
    2. Recursive case - defined in terms of 'smaller' version of itself
'''

'''
Recursive Procedures
'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)



'''
Quiz: Palindromes
    * Generally in Python it is less expensive to use non-recursive procedures
'''
def is_palindrome(s):
    if s == '':
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False


def iter_palindrome(s):
    for i in range(0, len(s) / 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True

'''
Quiz: Bunnies
    * Recursive functions for fibonacci is VERY inefficient!
'''
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# alternative solution
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

'''
Quiz: Faster Fibonacci
'''
def fibonacci(n):
    current = 0
    after = 1
    for i in range (0, n):
        current, after = after, current + after
    return current


'''
Circular Definitions
    * Circular definitions are horrible definitions because it never returns a value. Circular definitions do NOT have a clear base case.
'''

'''
Computer Ranks & Finishing Urank
'''
def compute_ranks(graph):
    d = 0.8             # damping factor - Probability that a random selected page is on the current page, rather than starting over with a new random page
    numloops = 10       # Determines the accuracy of the ranks

    ranks = {}
    npages = len(graph)

    for page in graph:
        ranks[page] = 1.0 / npages
    
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages

            for node in graph:
                if page in graph[node]:
                    newrank = newrank + d * (ranks[node] / len(graph[node]))
            
            newranks[page] = newrank
        ranks = newranks
    return ranks

