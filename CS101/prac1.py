myArray = [1,2,3,4,5,6,7]
arrayTotal = 0
for i in range(len(myArray)):
	arrayTotal +=myArray[i]
print(arrayTotal)


## =====================================================================
# Define a procedure, measure_udacity, that takes as its input a list
# of strings, and returns a number that is a count of the number
# of elements in the input list that start with the uppercase 
# letter 'U'.

def measure_udacity(p):
    sum = 0
    for i in p:
        if i[0] == 'U':
            sum = sum + 1
    return sum
        

print measure_udacity(['Dave','Sebastian','Umbrella'])
print measure_udacity(['Dave','Sebastian','Katy'])
print measure_udacity(['Umika','Umberto'])
print measure_udacity(['udacity','United Kingdom','U2', 'union'])

# ==========================================================================

# Define a procedure, find_element, that takes as its inputs a list
# and a value of any type, and returns the index of the first element
# in the input list that matches the value.
# If there is no matching element, return -1.

def find_element(aList, value):
    if value in aList:
        return aList.index(value)
    else :
        return -1
    
print find_element([1,2,3],3)
print find_element(['alpha','beta'],'gamma')


## =============== Alternate 1 =================================================
def find_element1(p,t):
        i = 0
        while i < len(p):
                if p[i] == t:
                        return i
                i = i + 1
        return -1

## =============== Alternate 2 ==================================================
def find_element2(p,t):
        i = 0
        for e in p:
                if e == t:
                        return i
                i = i + 1
        return -1
print find_element2([1,2,3],3)
print find_element2(['alpha','beta'],'gamma')
                
