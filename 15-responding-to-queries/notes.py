#############
#   Notes   #
# Lesson 15 #
#############
def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    # not found, add a new keyword
    index.append([keyword,[url]])

def lookup(index,keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return []

def add_page_to_index(index,url,content):
    words = content.split()
    for word in words:
        add_to_index(index,word,url)

'''
Latency - time it takes message to get from source to destination (usually measured in milliseconds 1000 milliseconds = 1 second)

Bandwidth - amount of information that can be transmitted per unit time (bits per second or million bits per second mbps)

What is a bit?
1 bit = smallest unit of information

As Brione points out, questions like this about how much information one bit conveys and what 
are the best questions to ask to get the most information are the heart of Information Theory.

'''