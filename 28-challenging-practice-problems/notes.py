#############
#   Notes   #
# Lesson 28 #
#############
'''
Quiz: Stirling and Bell
'''
def stirling(n, k):
    if n < k:
        return 0
    if n == k or k == 1:
        return 1
    return k*stirling(n-1, k) + stirling(n-1, k-1)

def bell(n):
    total = 0
    for k in range(1, n+1):
        total = total + stirling(n,k)
    return total

'''
Quiz: Combating Link Spam
'''
def is_reciprocal_link(graph, source, destination, k):
    if k == 0:
        if destination == source:
            return True
        return False
    if source in graph[destination]:
        return True
    for node in graph[destination]:
        if is_reciprocal_link(graph, source, node, k-1):
            return True
    return False

def compute_ranks(graph, k):
    d = 0.8 # damping factor
    numloops = 10
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    if not is_reciprocal_link(graph, node, page, k):
                        newrank = newrank + d * (ranks[node]/len(graph[node]))
            newranks[page] = newrank
        ranks = newranks
    return ranks

'''
Quiz: Elementary Cellular Automation
'''
