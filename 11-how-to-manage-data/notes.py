###########
## Notes ##
###########

'''
Unit 3: Data
String is a sequence of characters, while a list is a sequence of anything.
'''

'''
Quiz: Stooges
'''
stooges = ['Moe', 'Larry', 'Curly']

'''
Quiz: Days in a Month
'''
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

def how_many_days(month_number):
    return days_in_month[month_number - 1]

print how_many_days(1)
print how_many_days(9)

'''
Quiz: Countries
'''
capital_india = countries[1][1]
print capital_india

'''
Quiz: Relative Size
'''
print countries[0][2] / countries[2][2]

'''
Mutation & List of Strings
* Once an object is mutable we have to worry about other variables that might refer to the same object!
* Aliasing is when referring to the same object in two ways.
* Cannot mutate numbers or strings.
'''

'''
List Operations
* <list>.append(<element>) this adds a new element to the list by mutating it.
* len(<list>) - returns the number of elements in the list
* '+' adds the two lists together
'''

'''
How Computers Store Data
* In order to store data you need two things (1) something that preserves state, and (2) a way to read its state.
* bit is the fundamental unit of information, one bit is enough to decide between two options
* The fastest memory in your computer works like a switch. Data that is stored directly in the processor, which is called the register, is stored like a switch, which makes it very fast to change and read its state.
    * However, a register is like a light bulb in that when you turn the power off, you lose the state.
    * This means all the data stored in the register is lost when the computer is turned off.

* Another way the computers store data is similar to a bucket. We could represent a one by a full bucket and represent zero with an empty bucket.
* In computers, the buckets are holding electrons instead of water, and we call them capacitors. The memory in your computer that works that way is called DRAM.
* A gigabyte(2^30 or 2**30) gb means approximately a billion bytes. One byte is 8 bits.
    * In Python, the exponentiation operator is denoted with two asterisks:
    * <base> ** <power>
    kilobyte = 2 ** 10
    megabyte = 2 ** 20
    gigabyte = 2 ** 30
    terabyte = 2 ** 40

* What distinguises different types of memory is the time it takes to retrieve a value (this is called latency), the cost per bit, and how long it retains its state without poer.
    * for DRAM, the latency is about 12 nanoseconds (recall that there are one billion nanoseconds in a second).
'''

'''
For Loops
for <name> in <list>:
    <block>
'''
def sum_list(p)
    result = 0
    for e in p:
        result = result + e
    return result

def measure_udacity(U):
    count = 0
    for e in U:
        if e[0] == 'U':
            count = count + 1
    return count

# While loop is more natural choice because it keeps track of index
def find_element(p,t):
    i = 0
    while i < len(p):
        if p[i] == t:
            return i
        i = i + 1
    return -1

# For loop
def find_element(p,t):
    i = 0
    for el in p:
        if e == t:
            return i
        i = i + 1
    return -1

'''
<list>.index(<value>) - returns index
<value> (not) in <list> - returns boolean
'''
def find_element(p,t):
    if t in p:
        return p.index(t)
    else:
        return -1

'''
Quiz: Union
'''
def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

'''
<list>.pop() -> element
    * mutates the list by removing and returning its last element
'''

'''
Quiz: Crawl Web Loop
1. Polite
2. Multiple machines
3. Bandwidth
'''
def crawl_web(seed):
    to_crawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop() # this is a depth-first search because it searches from last to first, it's important to note the order of the pages searched matters a lot!
        if page not in crawled:
            union(tocrawl, get_all_links(get_page((page)))
            crawled.append(page)
    return crawled
