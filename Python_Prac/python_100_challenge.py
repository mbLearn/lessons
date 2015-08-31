###1
####Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
####between 2000 and 3200 (both included).
####The numbers obtained should be printed in a comma-separated sequence on a single line.
##
##i = []
##for x in range(2000, 3201):
##    if (x%7==0) and (x%5 != 0):
##        i.append(str(x))
##print ','.join(i)
##print '--------' * 12
##        
##
###2
####Write a program which can compute the factorial of a given numbers.
####The results should be printed in a comma-separated sequence on a single line.
####Suppose the following input is supplied to the program:
####8
####Then, the output should be:
####40320
##
##def factorial(x):
##    if x == 0:
##        return 1
##    return x * factorial(x-1)
##print "Enter the value here: "
##x = int(raw_input())
##print factorial(x)
##print '--------' * 12
##
###3
####With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
####Suppose the following input is supplied to the program:
####8
####Then, the output should be:
####{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
##
##def create_dict(x):
##    dict1 = {}
##    for i in range(1, x+1):
##        dict1[i] = i*i
##    return dict1
##print "Enter the number here: "
##x = int(raw_input())
##print create_dict(x)
##print '--------' * 12
##
###4
####Question:
####Write a program which accepts a sequence of comma-separated numbers from console and
####generate a list and a tuple which contains every number.
####Suppose the following input is supplied to the program:
####34,67,55,33,12,98
####Then, the output should be:
####['34', '67', '55', '33', '12', '98']
####('34', '67', '55', '33', '12', '98')
##
##print "Enter numbers here: "
##values = raw_input()
##list1 = values.split(",")
##set1 = tuple(list1)
##print list1, set1
##print '--------' * 12
##
###5
####Question:
####Define a class which has at least two methods:
####getString: to get a string from console input
####printString: to print the string in upper case.
####Also please include simple test function to test the class methods.
##
##
##class New():
##    def __init__(self):
##        self.s = ""
##    def get_string(self):
##        print "Enter you string here: "
##        self.s = raw_input()
##    def print_string(self):
##        print self.s.upper()
##    
##some_test = New()
##some_test.get_string()
##some_test.print_string()

#6
##Question:
##Write a program that calculates and prints the value according to the given formula:
##Q = Square root of [(2 * C * D)/H]
##Following are the fixed values of C and H:
##C is 50. H is 30.
##D is the variable whose values should be input to your program in a comma-separated sequence.
##Example
##Let us assume the following comma separated input sequence is given to the program:
##100,150,180
##The output of the program should be:
##18,22,24

import math
print "Add values here: "
c, h = 50, 30
list1 = [x for x in raw_input().split(',')]
new_list = []
for x in list1:
    new_x = str(int(math.sqrt((2*c*int(x))/h)))
    new_list.append(new_x)
print ','.join(new_list)

