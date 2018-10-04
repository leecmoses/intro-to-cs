#############
#   Notes   #
# Lesson 19 #
#############
'''
Quiz: Is Offered
'''
def is_offered(courses, course, hexamester):
    return course in courses_offered(courses, hexamester)

'''
Quiz: When Offered
'''
def when_offered(courses, course):
    offered = []
    for hexamester in courses:
        if course in courses[hexamester]:
            offered.append(hexamester)
    return offered

'''
Quiz: Involved
'''
def involved(courses, person):
    output = {}
    for hexamester in courses:
        for course in courses[hexamester]:
            for key in courses[hexamester][course]:
                if courses[hexamester][course][key] == person:
                    if hexamester in output:
                        output[hexamester].append(course)
                    else:
                        output[hexamester] = [course]
    return output

'''
Quiz: Refactoring
'''
def find_bucket(bucket,key):
    for entry in bucket:
        if entry[0] == key:
            return entry
    return None

def hashtable_update(htable, key, value):
    bucket = hashtable_get_bucket(htable, key)
    entry = find_bucket(bucket, key)
    if entry:
        entry[1] = value
    else:
        bucket.append([key, value])

def hashtable_lookup(htable, key):
    entry = find_bucket(hashtable_get_bucket(htable, key), key)
    if entry:
            return entry[1]
    return None

'''
Quiz: Memoization
'''
def cached_execution(cache, proc, proc_input):
    if proc_input not in cache:
        cache[proc_input] = proc(proc_input)
    return cache[proc_input]