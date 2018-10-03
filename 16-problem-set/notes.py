#############
#   Notes   #
# Lesson 16 #
#############
'''
Q: Data structures: How should we structure the index to track link click counts?
A: [[keyword,[url,count],[url,count]...]...]
'''

'''
Quiz: Better Splitting
'''
def split_string(source,splitlist):
    output = []
    atsplit = True # At a split point
    for char in source: # Iterate through string by each letter
        if char in splitlist:
            atsplit = True
        else:
            if atsplit:
                output.append(char)
                atsplit = False
            else:
                # Add character to last word
                output[-1] = output[-1] + char
    return output

'''
Quiz: Improving the Index
'''
def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            if not url in entry[1]: # solution is one line of code!
                entry[1].append(url)
            return

'''
Quiz: Counting Clicks
'''
def record_user_click(index,keyword,url):
    def record_user_click(index,keyword,url):
    urls = lookup(index, keyword)
    if urls:
        for entry in urls:
            if entry[0] == url:
                entry[1] = entry[1]+1

def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            for urls in entry[1]:
                if urls[0] == url:
                    return
            entry[1].append([url, 0])
            return
    # not found, add new keyword to index
    index.append([keyword, [[url, 0]]]) # The data structure of the entry has to change in order to accomodate for count!

'''
Quiz: Time Spent at Routers
'''
total_time = 75 # milliseconds traceroute, round trip Birminghan -> Sundavall
one_way_distance = 2500.0 # km Birminghan -> Sundavall
optic_speed = 200000 # km/s
ms_per_second = 1000 # conversion from ms to seconds [ms/sec]

# Calculations
time_on_the_wires = 2 * one_way_distance / optic_speed * ms_per_second
print time_on_the_wires
total_time_at_routers = total_time - time_on_the_wires
print total_time_at_routers