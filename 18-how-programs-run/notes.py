#############
#   Notes   #
# Lesson 18 #
#############

'''
Algorithm - is a procedure that always finishes and produces the correct result
Procedure - is a well defined sequence of steps that can be executed mechanically

Equivalent Expressions
* A property 'ord' and 'chr' is that they are inverses.
    * This means that if you input a single letter string to ord and then input the answer to chr, you get back the original single letter.
        * ord(<one-letter string>) -> Number
    * If you input a number to chr and then input the answer to that into ord, you get back the original number (as long as that number is within a certain range, 0 to 255 inclusive)
        * chr(<Number>) -> <one-letter string>
'''

'''
Quiz: Better Hash Functions
'''
# my solution
def hash_string(keyword,buckets):
    h = 0
    for c in keyword:
        h += ord(c)
    return h % buckets

# alternative solution
def hash_string(keyword,buckets):
    h = 0
    for c in keyword:
        h = (h + ord(c)) % buckets
    return h

'''
Quiz: Empty Hash Table
'''
def make_hashtable(nbuckets):
    i = 0
    table = []
    while i < nbuckets:
        table.append([])
        i += 1
    return table

# alternative solution
def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table

'''
Quiz: Find Buckets
'''
def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]

'''
Quiz: Adding Keywords
'''
def hashtable_add(htable,key,value):
    hashtable_get_bucket(htable,key).append([key, value])
    return htable


'''
Quiz: Lookup
'''
def hashtable_lookup(htable,key):
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket:
        if entry[0] == key:
            return entry[1]
    return None

'''
Quiz: Update
'''
# my solution
def hashtable_update(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    if hashtable_lookup(htable,key):
        for entry in bucket:
            if entry[0] == key:
                entry[1] = value
    else:
        hashtable_add(htable,key,value)
    return htable

# alternative solution
def hashtable_update(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket:
        if entry[0] == key:
            entry[1] = value
            return htable
    bucket.append([key, value])
    return htable

'''
Dictionaries
    String - sequence of characters (immutable)
    List - list of elements (mutable) []
    Dictionary - set of key-value pairs, <key, value> (mutable) {}
        * Essentially python's built-in hash function.
'''
