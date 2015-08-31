def stamps(n):
    p5 = n/5
    p2 =(n%5)/2
    p1 = (n%5)%2
    return p5,p2,p1

print stamps(8)
print stamps(5)
print stamps(29)

## ===================== Problem 2 =====================================-=======

# The range of a set of values is the maximum value minus the minimum
# value. Define a procedure, set_range, which returns the range of three
# input values.

def set_range(nums):
    maximum = minimun = nums[0] # Assume the first element is the max/min.
    for num in nums[1: ]:       # For each element in the rest of the list
        if num > maximum:       # If the current number is greater than the max
            maximum = num       # replace max
        else:                   # Current number is <= than the max
            if num < minimum:   # Check if it is less than the min
                minimum = num   # Replace min
    return maximum - minimum

## ====================== Problem 2a ==========================================
# works fine for few numbers. But you are iterating twice. Increases the
# amount of time to compute larger set of numbers. 
def set_range1(a,b,c):
    return max(a,b,c) - min(a,b,c)

## ======================= Problem 3 ==========================================
# Write a Python procedure fix_machine to take 2 string inputs
# and returns the 2nd input string as the output if all of its
# characters can be found in the 1st input string and "Give me
# something that's not useless next time." if it's impossible.

def fix_machine1(debris, product):
    list1 = []
    for char in list(product):
        if char in list(debris):
            newList = list1.append(char)
        else: 
            return "Give me something that's not useless next time."
    return product

# =================== Problem 3a better solution ===============================
def fix_machine2(debris,product):
    if set(list(product)).issubset(list(debris)):
           return product
    else:
           return "Give me something that's not useless next time."

## ================= Problem 3b even better solution ========================================
def fix_machine(debris, product):
    if any(debris.count(c) < product.count(c) for c in product):
        return "Give me something that's not useless next time."
    else: return product

### TEST CASES ###
print "Test case 1: ", fix_machine('UdaciousUdacitee', 'Udacity') == "Give me something that's not useless next time."
print "Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity') == 'Udacity'
print "Test case 3: ", fix_machine('AEIOU and sometimes y... c', 'Udacity') == 'Udacity'
print "Test case 4: ", fix_machine('wsx0-=mttrhix', 't-shirt') == 't-shirt'
print "Test case 5: ", fix_machine(' bedgih,onpsrut', 'oops, not enough debris') == "Give me something that's not useless next time."



## ======================= Problem 4 ==================================================================
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 

def is_leap_year(year, month):
    days = 0
    if year % 4 == 0 and month >= 3:
        days = 1
    return days

def leap_year_days(year1, year2):
    days = (year2 - year1) / 4
    return days
    
def daysInMonth(n):
    daysOfMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #for index, month in enumerate(daysOfMonth):
        #print index,month
    days = 0
    for i in range(n):
        days = days + daysOfMonth[i]
    return days

# Now figure out no. of leap years from year2 to year1. and add that many 1's to total. 
    
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    Total_days = (year2 - year1) * 365 + leap_year_days(year1, year2) + is_leap_year(year2, month2) +(daysInMonth(month2)-daysInMonth(month1)) + (day2 - day1)
    return Total_days

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
