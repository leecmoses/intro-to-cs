#########
# Notes #
#########
def product_list(p):
    total = 1
    for i in p:
        total = total * i
    return total

def greatest(p):
    greatest = 0
    for i in p:
        if i > greatest:
            greatest = i
    return greatest

def total_enrollment(p):
    total_students = 0
    total_tuition = 0
    for name, students, tuition in p:
        total_students = total_students + students
        total_tuition = total_tuition + students * tuition
    return total_students, total_tuition


'''
Quiz: Max Depth
'''
def crawl_web(seed,max_depth):    
    tocrawl = [seed]
    crawled = []
    next_depth = []
    depth = 0
    while tocrawl and depth <= max_depth:
        page = tocrawl.pop()
        if page not in crawled:
            union(next_depth, get_all_links(get_page(page)))
            crawled.append(page)
        if not tocrawl:
            tocrawl, next_depth = next_depth, []
            depth = depth + 1
    return crawled

'''
Quiz: Sudoku
'''
def check_sudoku(p):
    n = len(p) # Exact size of grid
    digit = 1 # start with 1
    while digit <= n: # Go through each digit
        i = 0
        while i < n: # Go through each row and column
            row_count = 0
            col_count = 0
            j = 0
            while j < n: #for each entry in ith row/column
                if p[i][j] == digit:
                    row_count = row_count + 1
                if p[j][i] == digit:
                    col_count = col_count + 1
                j = j + 1
            if row_count != 1 or col_count != 1:
                return False
            i = i + 1 # next row/column
        digit = digit + 1 # next digit
    return True # Nothing was wrong!
