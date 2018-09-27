##########
## Notes #
##########

'''
Problem 5
If s is the '' empty string, then s[0] will cause an error because there is no character at position 0.
This is called an edge case in programming, It's a situation that doesn't come up too often (you usually don't need to use an empty string), but it does happen sometime.
It's easy to forget about edge cases and doing so is a common cause of bugs.
'''

'''
Problem 7
The method .find() returns the lowest index of the substring if it is found in given string. If it's not found then it returns -1.
'''

'''
Problem 8
'''
text = 'zip files are zipped'
first_zip = text.find('zip')
print(text.find('zip', first_zip + 1))

'''
Problem 9
Use str() to turn a number into a string.
'''
