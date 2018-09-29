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
5. Develop incrementally and test as we go!
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
def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def daysInMonth(year, month):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    else:
        if month == 2:
            if isLeapYear(year):
                return 29
            else:
                return 28
    return 30

def nextDay(year, month, day):
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        day += 1
    return days