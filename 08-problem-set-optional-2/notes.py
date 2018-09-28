###########
## Notes ##
###########
'''
Quiz: Superhero Nuisance
'''
# def fix_machine(debris, product):
#     p = product
#     while p != '':
#         if debris.find(p[0]) == -1:
#             return 'Give me something that\'s not useless next time.'
#         p = p[1:] # remove the first character this copies every character except the first character
#     return product

# Alternative solution

def fix_machine(d, p):
    return p if set(p) <= set(d) else 'Give me something that\'s not useless next time.'

'''
Quiz: Days Old
Need to review again!! This one was tough to solve!
'''
def isLeapYear(year):
    # From Wikipedia http://en.wikipedia.org/wiki/Leap_year
    """
    if (year is not exactly divisible by 4) then (it is a common year)
    else
    if (year is not exactly divisible by 100) then (it is a leap year)
    else
    if (year is not exactly divisible by 400) then (it is a common year)
    else (it is a leap year)    
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True 
    else:
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
        else:
            return 30

def nextDay(year, month, day):
    # Use correct number of days per month
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1           
        else:
            return year + 1, 1, 1
        
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    # Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False.
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Returns the number of days between year1/month1/day1
    and year2/month2/day2. Assumes inputs are valid dates
    in Gregorian calendar.
    """
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

'''
Quiz: 10 Row Abacus
Need to review again!! This one was tough to solve!
'''
def print_abacus(value):
    a = "0" * (10 - len(str(value))) + str(value); b = "00000*****"
    for c in range(10): print "|" + b[:len(b) - int(a[c])] + "   " + b[len(b) - int(a[c]):] + "|"


'''
Quiz: Jungle Animal
'''
def jungle_animal(animal, my_speed):
    if animal == "zebra":
        print "Try to ride a zebra!"
    elif animal == "cheetah":
        if my_speed > 115:
            print "Run!"
        else:
            print "Stay calm and wait!"
    else:
        print "Introduce yourself!"

'''
Quiz: Leap Year Baby
'''
def is_leap_baby(day,month,year):
    is_leap_year = year % 400 == 0 or (year % 100 != 0 and year % 4 ==0)
    return is_leap_year and ((day, month) == (29, 2))