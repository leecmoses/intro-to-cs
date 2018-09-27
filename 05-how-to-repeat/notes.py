###########
## Notes ##
###########
'''
Here is the Python grammar for writing a procedure:
def <name>(<params>):
    <block>
'''

'''
Quiz: Find Second
'''
def find_second(search, target):
    first = search.find(target)
    return search.find(target, first + 1)

'''
Quiz: Is Friend & More Friends
<expression> or <expression>
* If the first expression evaluates to True, the value is True and the second expression is not evaluated.
* If the first expression evaluates to False, then value is the value of the second expression.
'''
def is_friend(name):
    return name[0] == 'D'

'''
Quiz: Biggest
* This works the same as Python's build in method, max().
'''
def biggest(x, y, z):
    if x > y:
        if x > z:
            return x
        else:
            return z
    else:               # y >= x
        if y > z:
            return y
        else:           # z >= y >= x
            return z

print(biggest(9, 3, 9))


'''
Quiz: Factorial
* Recall that the factorial of a number is calculated by multiplying all the integers from 1 to that number together.
'''
def factorial(n):
    result = 1
    while n >= 1:
        result = result * n
        n = n - 1
    return result

'''
Quiz: Multiple Assignment
s, t = t, s
* This swaps the values of s and t
'''