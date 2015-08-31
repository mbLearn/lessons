# Define a procedure, product_list, takes as input a list of numbers,
# and returns a number that is the result of multiplying all
# those numbers together.

def product_list(p):
    product = 1
    for e in p:
        product = product * e
    return product

print product_list([9])
print product_list([1,2,3,4])
print product_list([])

# ============================== Alternative =============================
def product_list1(p):
    return 1 if p == [] else p.pop() * product_list1(p)

print product_list1([9])
print product_list1([1,2,3,4])
print product_list1([])

# ======================= Alternative 2 =================================
def product_list2(lst):
    return reduce(lambda x, y: x * y, lst or [1])

## In English: Take the list L; or if the value of L is None, take the list
# [1] instead. Take the function "multiply two numbers". Apply the function
# to the first two values in the list, then apply the function to the
# previous result and the third value in the list, then to the previous
# result and the fourth value in the list...and so on, until the end
# of the list. Return the final result.

# "lambda x,y: something" means: a function that takes two values (x and y)
# and returns something.

# "reduce some_function some_list" means: use the function to the first two
# values of the list, then the result and the third value, then the result
# and the fourth value... and the last value. For example, if the function
# is plus, applying in to the list [1, 2, 3, 4] means ((1+2)+3)+4.


### =========================Problem =======================================
# Define a procedure, greatest, that takes as input a list of positive
# numbers, and returns the greatest number in that list. If the input
# list is empty, the output should be 0.

def greatest(lst):
    return 0 if lst == [] else max(lst)

# ======================= Alternate ===========================================
def greatest1(lst, current_max=0):
    if lst == []:
        return current_max
    elif lst[0] > current_max:
        return greatest1(lst[1:], lst[0])
    else:
        return greatest1(lst[1:], current_max)

print greatest1([4,23,11,34,655,2323,5])


## ============================= Alternate ================================
def greatest2(lst):
    big = 0
    for i in lst:
        if i > big:
            big = i
    return big
print greatest2([3,4,2,56,12,122])

## ============================= Problem ==================================        
# Define a procedure, total_enrollment, that takes as an input a list of
# elements, where each element is a list containing three elements: a
# university name, the total number of students enrolled and the annual
# tuition fees.

# The procedure should return two numbers, not a string, giving the total
# number of students enrolled at all of the universities in the list,
# and the total tuition fees (which is the sum of the number
# of students enrolled times the tuition fees for each university).

udacious_univs = [['Udacity',90000,0]]

usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]


def total_enrollment(lst):
    total_students = 0
    total_tuition = 0
    for i in lst:
        total_tuition = total_tuition + (i[1] * i[2])
        total_students = total_students + i[1]
    return total_students, total_tuition

print total_enrollment(udacious_univs)
print total_enrollment(usa_univs)
#>>> (77285,3058581079L)
# The L is automatically added by Python to indicate a long number.

## =============== Alternate ==========================================


def total_enrollment1(lst):
    total_students = 0
    total_tuition = 0
    for name,students,fees in lst:
        total_tuition = total_tuition + (students * fees)
        total_students = total_students + students
    return total_students, total_tuition

print total_enrollment1(usa_univs)


## ===================== Sudoku =======================================
# Define a procedure, check_sudoku, that takes as input a square list
# of lists representing an n x n sudoku puzzle solution and returns the
# boolean True if the input is a valid sudoku square and returns the
# boolean False otherwise.

# A valid sudoku square satisfies these two properties:

# 1. Each column of the square contains each of the whole numbers
#    from 1 to n exactly once.
# 2. Each row of the square contains each of the whole numbers
#    from 1 to n exactly once.

# You may assume the the input is square and contains at least one row
# and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
def check_sudoku(lst):
    range_lst = range(1,len(lst) + 1)
    for i in lst:
        if sorted(i) != range_lst: return False
    for i in range(len(lst)):
        sudoku_column = []
        for m in lst:
            sudoku_column.append(m[i])
        if sorted(sudoku_column) != range_lst : return False
    return True

    
print check_sudoku(incorrect)
print check_sudoku(correct)
print check_sudoku(incorrect2)
print check_sudoku(incorrect3)
print check_sudoku(incorrect4)
print check_sudoku(incorrect5)


# ================== Alternate Sudoku =================================
def check_sudoku1(p):
    n = len(p)                   # Extract size of grid
    digit = 1                    # start with 1
    while digit <= n:            # Go through each digit
        i = 0
        while i < n:             # Go through each row and column
            row_count = 0
            col_count = 0
            j = 0
            while j < n:   # for each entry in ith row/column
                if p[i][j] == digit:    # check row count
                    row_count = row_count + 1
                if p[j][i] == digit:
                    col_count = col_count + 1
                j = j + 1
            if row_count != 1 or col_count != 1:
                return False
            i = i + 1   # next row / column
        digit = digit + 1
    return True

print check_sudoku1(incorrect)
print check_sudoku1(correct)
print check_sudoku1(incorrect2)
print check_sudoku1(incorrect3)
print check_sudoku1(incorrect4)
print check_sudoku1(incorrect5)

                


