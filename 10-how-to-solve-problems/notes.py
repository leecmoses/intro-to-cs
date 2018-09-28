###########
## Notes ##
###########
'''
Q: What is the first thing we should do to solve a problem like this one?
A: Make sure we understand the problem

Understanding a Computational Problem
* Problem is defined by the relationship between possible inputs and desired outputs
* Solution is defined by the procedure

Pythonista's Guide to All Problems in the Galaxy
0. Don't panic!!
1. What are the inputs?
2. What are the outputs?
3. Work through some examples by hand
4. Simple mechanical solution
* work out examples to understand the relationship between inputs and outputs
* consider systematically how a human solves the problem
* write in pseudocode
* Don't optimize prematurely!
'''
# def nextDay(year, month, day):
#     """
#     Returns the year, month, day of the next day.
#     Simple version: assume every month has 30 days.
#     """
#     if day < 30:
#         day += 1
#     elif day == 30:
#         day = 1
#         month += 1
#         if month > 12:
#             month = 1
#             year += 1
#     return year, month, day

#  Alternatively
def nextDay(year, month, day):
    if day < 30:
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1
