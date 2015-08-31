## ======================= Recursive Method ===================================
## ======================= probelm 1 - Factorial ==============================
# Define a procedure, factorial, that takes a natural number as its input, and
# returns the number of ways to arrange the input number of items.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print factorial(0)
print factorial(6)
print factorial(10)

## ================= Problem 2 - Palindromes =====================================
print "\n"
# Define a procedure is_palindrome, that takes as input a string, and returns a
# Boolean indicating if the input string is a palindrome.

# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?

def is_palindrome(s):
    if s == '':
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])

print is_palindrome('')
#>>> True
print is_palindrome('abab')
#>>> False
print is_palindrome('abba')
#>>> True

## ==================== Alternative without Recursion =================
def inter_palindrome(s):
    for i in range(0,len(s) /2):
        if s[i] != s[-(i + 1)]:
            return False
    return True

## for long words and sentences this is the efficient and cheaper solution.
## Recursion in Python is expensive. Consumes more memory. 


## =========================== Problem 3 - Fibonacci =======================
print "\n"
# Define a procedure, fibonacci, that takes a natural number as its input, and
# returns the value of that fibonacci number.

# Two Base Cases:
#    fibonacci(0) => 0
#    fibonacci(1) => 1

# Recursive Case:
#    n > 1 : fibonacci(n) => fibonacci(n-1) + fibonacci(n-2)


def fibonacci1(n):
    if n < 2:
        return n
    else:
        return fibonacci1(n-1) + fibonacci1(n-2)

## ======================== Iterative Alternative ==============================
#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    sum1,sum2 = 0,1
    x = 0
    while x < n:
        sum1, sum2 = sum2, sum1 + sum2
        x = x + 1
    return sum1
   

print fibonacci(0)
print fibonacci(1)
print fibonacci(5)
print fibonacci(36)
#>>> 14930352

## ======================== Iterative Alternative ==============================
def fibonacci2(n):
    sum1,sum2 = 0,1
    for i in range(0,n):
        sum1, sum2 = sum2, sum1 + sum2
    return sum1
print fibonacci(10)


## ==============================================================================
# Rabbits Multiplying

# A (slightly) more realistic model of rabbit multiplication than the Fibonacci
# model, would assume that rabbits eventually die. For this question, some
# rabbits die from month 6 onwards.
#
# Thus, we can model the number of rabbits as:
#
# rabbits(1) = 1 # There is one pair of immature rabbits in Month 1
# rabbits(2) = 1 # There is one pair of mature rabbits in Month 2
#
# For months 3-5:
# Same as Fibonacci model, no rabbits dying yet
# rabbits(n) = rabbits(n - 1) + rabbits(n - 2)
#
#
# For months > 5:
# All the rabbits that are over 5 months old die along with a few others
# so that the number that die is equal to the number alive 5 months ago.
# Before dying, the bunnies reproduce.
# rabbits(n) = rabbits(n - 1) + rabbits(n - 2) - rabbits(n - 5)
#
# This produces the rabbit sequence: 1, 1, 2, 3, 5, 7, 11, 16, 24, 35, 52, ...
#
# Define a procedure rabbits that takes as input a number n, and returns a
# number that is the value of the nth number in the rabbit sequence.
# For example, rabbits(10) -> 35. (It is okay if your procedure takes too
#                                long to run on inputs above 30.)

def rabbits(n):
    if n < 2:
        return n
    elif n <= 5:
        return rabbits(n - 1) + rabbits(n - 2)
    else:
        return rabbits(n - 1) + rabbits(n - 2) - rabbits(n - 5)

print rabbits(10)


## ======================= Alternative =======================================
def rabbits2(n):
    current = 1
    future = 0
    rabbit_history = []
    
    for i in range(0,n):
        current, future = future, current + future
        if len(rabbit_history) >= 5:
            future = future - rabbit_history[-5]
        rabbit_history.append(future)
    return rabbit_history[n-1]

print rabbits2(30)


## ===============================================================================
# Spreading Udaciousness
 
# One of our modest goals is to teach everyone in the world to program and
# understand computer science. To estimate how long this will take we have
# developed a (very flawed!) model:

# Everyone answering this question will convince a number, spread, (input to 
# the model) of their friends to take the course next offering. This will 
# continue, so that all of the newly recruited students, as well as the original
# students, will convince spread of their
# friends to take the following offering of the course.
# recruited friends are unique, so there is no duplication among the newly
# recruited students. Define a procedure, hexes_to_udaciousness(n, spread,
# target), that takes three inputs: the starting number of Udacians, the spread
# rate (how many new friends each Udacian convinces to join each hexamester),
# and the target number, and outputs the number of hexamesters needed to reach 
# (or exceed) the target.

# For credit, your procedure must not use: while, for, or import math. 

def hexes_to_udaciousness(n, spread, target):
    if n >= target:   #Base Case
        return 0
    else:           #Recursive Call
        return 1 + hexes_to_udaciousness(n + spread * n, spread, target)



# 0 more needed, since n already exceeds target
print hexes_to_udaciousness(100000, 2, 36230) 
#>>> 0

# after 1 hexamester, there will be 50000 + (50000 * 2) Udacians
print hexes_to_udaciousness(50000, 2, 150000) 
#>>> 1 

# need to match or exceed the target
print hexes_to_udaciousness(50000, 2, 150001)
#>>> 2 

# only 12 hexamesters (2 years) to world domination!
print hexes_to_udaciousness(20000, 2, 7 * 10 ** 9) 
#>>> 12 

# more friends means faster world domination!
print hexes_to_udaciousness(15000, 3, 7 * 10 ** 9)
#>>> 10 


## ========================================================================


def is_list(p):
    return isinstance(p, list)

def deep_count(p):
    if is_list(p) == False:
        return 0
    elif p == []:
        return 0
    else:
        for i in p:
            result = len(p) + deep_count(i)
    return result

## ========================================================================
def deep_count1(p):
    sum = 0
    for e in p:
        if is_list(e):
            sum = sum + deep_count1(e)
    return e

## ========================================================================
##logic
##def deep_count(p):
##    if is_list(p):
##        length = len(p)
##        for n in range(len(p)):
##            print p[n]
##            if is_list(p[n]):
##                inner_length = len(p[n])
##                length = length + inner_length
##                for m in range(len(p[n])):
##                               if is_list(p[n][m]):
##                                   inner_inner_len = len(p[n][m])
##                                   length = length + inner_inner_len
##                               

        
    
