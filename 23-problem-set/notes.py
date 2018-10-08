#############
#   Notes   #
# Lesson 23 #
#############
'''
Quiz: Rabbits Multiplying
'''
def rabbits(n):
    if n < 1:
        return 0
    else:
        if n == 1 or n == 2:
            return 1
        else:
            return rabbits(n-1) + rabbits(n-2) - rabbits(n-5)

'''
Quiz: Spreading Udaciousness
'''
def hexes_to_udaciousness(n, spread, target):
    if n >= target:
        return 0
    else:
        return 1 + hexes_to_udaciousness(n * (1 + spread), spread, target)

'''
Quiz: Deep Count
'''
def deep_count(p):
    sum = 0
    for e in p:
        sum += 1
        if is_list(e):
            sum = sum + deep_count(e)
        return sum

'''
Quiz: Feeling Lucky
'''
def lucky_search(index, ranks, keyword):
    pages = lookup(index, keyword)
    if not pages:
        return None
    best_page = pages[0]
    for candidate in pages:
        if ranks[candidate] > ranks[best_page]:
            best_page = candidate
    return best_page