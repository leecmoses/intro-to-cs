###########
## Notes ##
###########

'''
The replace() method returns a copy of the string where all occurrences of a substring is replaced with another substring.

The syntax of replace() is:
str.replace(old, new[, count])

replace() parameters
    * old - old substring you want to replace
    * new - new substring which you would replace the old substring
    * count (optional) - the number of times you want to replace the old substring with the new substring

If count is not specified, replace() method replaces all occurrences of the old substring with the new substring
'''

'''
Problem 5
Remember to use python 2.7, not python 3 for this problem
'''
print (10/4.0)
print (10/4)
print (10.0/5)
print (10 * 1.0 / 4)
print (10 / 5)
print (10 / 50)

'''
Problem 6
You can read a string backwards with the following syntax:
string[::-1] - where the "-1" means one step back.
'''
word = 'madman'
reverse = word[::-1]
is_palindrome = word.find(reverse) 