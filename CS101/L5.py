import time

def time_execution(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

def spin_loop(n):
    i = 0
    while i < n:
        i = i + 1

## ======================= Defining a hash_string ======================
# Define a function, hash_string, that takes as inputs a keyword (string)
# and a number of buckets, and returns a number representing the bucket
# for that keyword.

def hash_string(keyword,buckets):
    total = 0
    for i in keyword:
        total = (total + ord(i)) % buckets
    return total  


print hash_string('a',12)

print hash_string('b',12)

print hash_string('a',13)

print hash_string('au',12)

print hash_string('udacity',12)

## ===================== One liner Alterntive ==============================
def hash_string1(keyword, buckets):
    return reduce(lambda x,y: x + y, [ord(x) for x in keyword], 0) % buckets

## ===================== ALternative ========================================
def has_string2(keyword, buckets):
    return sum([ord(x) for x in keyword]) % buckets

# The parentheses are needed for and part of the built-in function sum().
# sum() returns the sum of a sequence of numbers in an iterable.
# A list is an iterable, so we can use sum([1, 2]) and get a result 3.
# In this particular case I use a so-called list comprehension, which
# returns a list of ord() numbers for each letter in keyword.
# We then pass that list to sum() and use modulo to get our answer.

## ================ Create empty hash table ================================
print "\n"
# Creating an Empty Hash Table. Define a procedure, make_hashtable,
# that takes as input a number, nbuckets, and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
    index = []
    n = 0
    while n < nbuckets:
        index.append([])
        n = n + 1
    return index

print make_hashtable(1)

# ============================ Alternative ====================================
print '\n'

def make_hashtable1(nbuckets):
    index = []
    while len(index) < nbuckets:
        index.append([])
    return index

print make_hashtable1(1)
print make_hashtable1(10)

# ========================= Alternative ======================================
def make_hashtable2(nbuckets):
    return [[] for x in range(nbuckets)]

## ===================== Alternative ==========================================
print "\n"
def make_hashtable3(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table

print make_hashtable3(1)
print make_hashtable3(10)
    
## ===================== Hashtable_get_bucket ===============================
print "\n"

# Define a procedure, hashtable_get_bucket, that takes two inputs - a hashtable, and
# a keyword, and returns the bucket where the keyword could occur.

def hashtable_get_bucket(htable,keyword):
    bucket = hash_string(keyword,len(htable))
    return htable[bucket]

table = [[['Francis', 13], ['Ellis', 11]], [], [['Bill', 17],
['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]]

print hashtable_get_bucket(table, "Zoe")
#>>> [['Bill', 17], ['Zoe', 14]]

print hashtable_get_bucket(table, "Brick")
#>>> []

print hashtable_get_bucket(table, "Lilith")
#>>> [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]

## ========================== hashtable_add  ==================================
print "\n"

# Define a procedure, hashtable_add(htable,key,value)
#
# that adds the key to the hashtable (in the correct bucket), with the correct 
# value and returns the new hashtable.
#
# (Note that the video question and answer do not return the hashtable, but
# your code should do this to pass the test cases.)

def hashtable_add(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    bucket.append([key,value])
   

table = make_hashtable(5)
hashtable_add(table,'Bill', 17)
hashtable_add(table,'Coach', 4)
hashtable_add(table,'Ellis', 11)
hashtable_add(table,'Francis', 13)
hashtable_add(table,'Louis', 29)
hashtable_add(table,'Nick', 2)
hashtable_add(table,'Rochelle', 4)
hashtable_add(table,'Zoe', 14)
print table

## ====================  hashtable_lookup(htable,key) =============================
print '\n'
# Define a procedure, hashtable_lookup(htable,key) that takes two inputs,
# a hashtable and a key (string),and returns the value associated with that key.

def hashtable_lookup(htable,key):
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket:
            if entry[0] == key:
                return entry[1]
    return None

table = [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
[['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

print hashtable_lookup(table, 'Francis')
#>>> 13

print hashtable_lookup(table, 'Louis')
#>>> 29
