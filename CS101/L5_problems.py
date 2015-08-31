## ==================== has_duplicate_element ==============================
def has_duplicate_element(p):
    res = []
    for i in range(0,len(p)):
        for j in range(0,len(p)):
            if i != j and p[i] == p[j]:
                return True
    return False

## ====================== Is_offered ============================================
print "\n"
# Dictionaries of Dictionaries (of Dictionaries)

# The next several questions concern the data structure below for keeping
# track of Udacity's courses (where all of the values are strings):

#    { <hexamester>, { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }

#For example,

courses = {
    'feb2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'apr2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': 
                {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': 
                {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'jan2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                 'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }

# If you want to loop through the keys in the dictionary,
# you can use the construct below.
#         for <key> in <dictionary>:
#                    <block>  
# For example, this procedure returns a list of all the courses offered 
# in the given hexamester:

def courses_offered(courses, hexamester):
    res = []
    for c in courses[hexamester]:
        res.append(c)
    return res

# You do not need to use this code if you do not want to and may find another, 
# simpler method to answer this question, although later ones may require this.

# Define a procedure, is_offered(courses, course, hexamester), that returns 
# True if the input course is offered in the input hexamester, and returns 
# False otherwise.  For example,

#print is_offered(courses, 'cs101', 'apr2012')
#>>> True

#print is_offered(courses, 'cs003', 'apr2012')
#>>> False

# (Note: it is okay if your procedure produces an error if the input 
# hexamester is not included in courses.
# For example, is_offered(courses, 'cs101', 'dec2011') can produce an error.)
# However, do not leave any uncommented statements in your code which lead 
# to an error as your code will be graded as incorrect.

def is_offered(courses, course, hexamester):
    course_lst = courses_offered(courses, hexamester)
    if course in course_lst: 
        return True
    return False


print is_offered(courses, 'cs101', 'apr2012')
#>>> True

print is_offered(courses, 'cs003', 'apr2012')
#>>> False

print is_offered(courses, 'cs001', 'jan2044')
#>>> True

print is_offered(courses, 'cs253', 'feb2012')
#>>> False

## =======================    Alternative     ================================
print "\n"
def is_offered1(courses, course, hexamester):
    return course in courses[heaxamester]

## =============================== Problem 3 ===================================
print "\n"
# Define a procedure, when_offered(courses, course), that takes a courses data
# structure and a string representing a class, and returns a list of strings
# representing the hexamesters when the input course is offered.

def when_offered(courses,course):
    name_course = []
    for key,value in courses.items():
        for name,properties in value.items():
            if name == course:
                name_course.append(key)
    return name_course


print when_offered (courses, 'cs101')
#>>> ['apr2012', 'feb2012']

print when_offered(courses, 'bio893')
#>>> []

## ========================== Alternative ======================================
def when_offered(courses, course):
    offered = []
    for hexamester in course:
        if course in courses[hexamester]:
            offered.append(hexamester)
    return offered
            
