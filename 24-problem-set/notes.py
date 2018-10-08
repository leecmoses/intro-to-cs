#############
#   Notes   #
# Lesson 24 #
#############
'''
Quiz: Family Trees
    * Input: dictionary {child:[parent1, parent2]}
    * Output: list of all ancestors

Plan
    1) Find person in dictionary
    2) Add parents to output
    3) Recurse on parents to find ancestors
'''
def ancestors(genealogy, person):
    if person in genealogy:
        parents = genealogy[person]
        result = parents
        for parent in parents:
            result = result + ancestors(genealogy, parent)
        return result
    
    return [] # no ancestors known

'''
Quiz: Khayyam Triangle
    * Input: number of rows in triangle
    * Output: list of list of numbers

Plan
    1) Create first row
    2) Write a helper function that creates the next row
'''
def make_next_row(row):
    result = []
    prev = 0
    for e in row:
        result.append(e + prev)
        prev = e
    result.append(prev)
    return result

def triangle(n):
    result = []
    current = [1]
    for unused in range(0,n):
        result.append(current)
        current = make_next_row(current)
    
    return result

'''
Quiz: Only a Little Lucky
    * Input: index, ranks, and keyword
    * Output: ordered list of urls
'''
def ordered_search(index, ranks, keyword):
    if keyword not in index:
        return None
    return sorted(index[keyword], key=lambda e:ranks[e], reverse=True)