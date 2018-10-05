#############
#   Notes   #
# Lesson 20 #
#############
'''
Quiz: Shift a Letter
'''
def shift(letter):
    if ord(letter) + 1 <= 122:
        return chr(ord(letter) + 1)
    else:
        return 'a'

'''
Quiz: Shift a Letter
'''
def shift_n_letters(letter, n):
    letter_index = ord(letter) - ord('a') # one of 0, 1, 2, ..., 25
    shifted_index = (letter_index + n) % 26 # still one of 0, 1, 2, ..., 25
    return chr(ord('a') + shifted_index)

'''
Quiz: Rotate
'''
def rotate(str,n):
    letters = list(str)
    i = 0
    for letter in letters:
        if letter == ' ':
            letters[i] = ' '
        else:
            letter_index = ord(letter) - ord('a')
            shifted_index = (letter_index + n) % 26
            letters[i] = chr(ord('a') + shifted_index)
        i += 1
    return ''.join(letters)

# alternative solution using helper function from previous exercise
def shift(letter, n):
    letter_index = ord(letter) - ord('a')
    shifted_index = (letter_index + n) % 26
    return chr(ord('a') + shifted_index)

def rotate(s, n):
    return ''.join(c if c == ' ' else shift(c, n) for c in s)