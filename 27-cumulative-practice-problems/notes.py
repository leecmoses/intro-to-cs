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


'''
Quiz: Date Converter
Input - dictionary and string
Output - string with date in appropriate language

Plan
    1) Create a variable for the day, month, and year
    2) Use month variable as the key to call the correct value
    3) Return concatenated string
'''
def date_converter(language, date):
    first = date.find('/')
    month = date[:first]
    second = date.find('/', first + 1)
    day = date[first + 1 : second]
    year = date[second + 1:]
    return day + ' ' + language[int(month)] + ' ' + year

# Alternative solution using the split method
def date_converter2(language, date):
    month, day, year = date.split('/')
    return day + ' ' + language[int(month)] + ' ' + year

'''
Quiz: Termination
'''

def proc1(n):
   while True:
      n = n - 1
      if n == 0:
         break
   return 3

def proc2(n):
   if n == 0:
      return n
   return 1 + proc2(n - 2)

def proc3(n):
   if n <= 3:
      return 1
   return proc3(n - 1) + proc3(n - 2) + proc3(n - 3)


'''
Quiz: Find and Replace
'''
def apply_converter(converter, string):
previous = None
while previous != string:
    previous = string
    position = string.find(converter[0])
    if position != -1:
        string = string[:position] + converter[1] + string[position + len(converter[0]):]
return string

'''
Quiz: Longest Repetition
'''
def longest_repetition(input_list):
    best_element = None
    best_length = 0
    current_element = None
    current_length = 0
    for element in input_list:
        if element != current_element:
            current_element = element
            current_length = 1
        else:
            current_length += 1
        if current_length > best_length:
            best_length = current_length
            best_element = current_element
    return best_element


'''
Quiz: Deep Reverse
'''
def deep_reverse(p):
    if is_list(p):
        result = []
        for i in range(len(p) - 1, -1, -1): #range stops one before the number because we want to stop at 0 that is why -1 is used as the end range.
            result.append(deep_reverse(p[i]))
        return result
    else:
        return p
