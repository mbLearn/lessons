# ===================== Problem 1 ================================
# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median1(a,b,c):
    if (a != biggest(a,b,c)) and (b != biggest(a,b,c)):
        return bigger(a,b)
    elif (b != biggest(a,b,c)) and (c != biggest(a,b,c)):
        return bigger(b,c)
    else:
        return bigger(a,c)

# alternate solution:

def median(a,b,c):
    big = biggest(a,b,c)
    if a == big:
        return bigger(b,c)
    elif b == big:
        return bigger(a,c)
    else:
        return bigger(a,b)


## ======================= Problem 2 =============================
# out a countdown from that number to 1,
# followed by Blastoff!
# The procedure should not return anything.
# For this question, you just need to call 
# the procedure using the line
# countdown(3)
# instead of print countdown(3).

def countdown(n):
    
    while n == 0:
        print n
        n = n - 1
    print "Blastoff!"



## =========================================================================
# Check if following loops always finish or sometimes run forever or unknown
# Loop 1 - ALWAYS FINISHES

def loop1(n):
    i = 0
    while i <= n:
        i = i + 1
        print n, i
    
# ==========================================================================
# Loop 2 - ALWAYS FINISHES
def loop2(n):
    i = 1
    while True:
        i = i * 2
        n = n + 1
        if i > n:
            break
        print n, i

## ======================================================================
# Loop 3 - UNKNOWN (TO ANYONE)
def loop3(n):
    while n != 1:
        if n % 2 == 0:
            n  = n/2
        else:
            n = 3 * n + 1
        print n

## ========================Problem 4============================
# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

def find_last(s1, s2):
    result = 0
    while s1.find(s2, result) >= 0:
        result = result + 1
    else:
        return result -1

## Alternate solution
def find_last1(s1, s2):
    last_pos = -1
    while True:
        pos = s1.find(s2, last_pos + 1)
        if pos == -1:
            return last_pos
        last_pos = pos


## Define a procedure that takes as input a positive whole number, and
## prints out a multiplication table, showing all the whole number multiplications
## up to and including the input number.

def print_multiplication_table(n):
    i = 1
    while i <= n:
        j = 1
        while j <= n:
            print str(i) + "*" + str(j) + "=" + str(i*j)
            j = j + 1
        i = i + 1
