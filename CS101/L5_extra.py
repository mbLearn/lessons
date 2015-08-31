## =============== Problem 1 ==================================================
# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a' 
# following 'z'.

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',\
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def shift(letter):
    for value in alphabets:
        if value == letter:
            index_value = alphabets.index(value)
            if index_value == 25:
                return alphabets[0]
            else:
                return alphabets[ index_value + 1]
                                
     

print shift('a')
#>>> b
print shift('n')
#>>> o
print shift('z')
#>>> a

## ========================== Problem 2 =====================================
print '\n'
# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift_n_letters(letter, n):
        for value in alphabets:
            if value == letter:
                index_value = alphabets.index(value)
                new_index = index_value + n
                if new_index > 25:
                    new_index = new_index - 26
                return alphabets[new_index]

                
print shift_n_letters('s', 1)
#>>> t
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('s', -10)
#>>> i


## =======================     Rotate     ====================================
print '\n'
# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string
# constructed by shifting each of the letters n steps, and leaving the spaces
# unchanged. Note that 'a' follows 'z'. You can use an additional procedure if
# you choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def rotate(string1, n):
    new_string = ''
    for letter in string1:
        if letter == ' ':
            new_string += ' '
        else:
            new_string += shift_n_letters(letter, n)
    return new_string

print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)

## =============== Dictionary Example ================================================
print '\n'
# [Double Gold Star] Memoization is a way to make code run faster by saving
# previously computed results.  Instead of needing to recompute the value of an
# expression, a memoized computation first looks for the value in a cache of
# pre-computed values.

# Define a procedure, cached_execution(cache, proc, proc_input), that takes in
# three inputs: a cache, which is a Dictionary that maps inputs to proc to
# their previously computed values, a procedure, proc, which can be called by
# just writing proc(proc_input), and proc_input which is the input to proc.
# Your procedure should return the value of the proc with input proc_input,
# but should only evaluate it if it has not been previously called.

def cached_execution(cache, proc, proc_input):
    # format of cache {proc_input1 : proc_output1, proc_input2: proc_output2, ..}
    if proc_input not in cache:
        result = proc(proc_input)
        cache[proc_input] = result
    return cache[proc_input]


# Here is an example showing the desired behavior of cached_execution:

def factorial(n):
    print "Running factorial"
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result

cache = {} # start cache as an empty dictionary
### first execution (should print out Running factorial and the result)
print cached_execution(cache, factorial, 50)

print "Second time:"
### second execution (should only print out the result)
print cached_execution(cache, factorial, 50)

# Here is a more interesting example using cached_execution
# (do not worry if you do not understand this, though,
# it will be clearer after Unit 6):

def cached_fibo(n):
    if n == 1 or n == 0:
        return n
    else:
        return (cached_execution(cache, cached_fibo, n - 1 )
               + cached_execution(cache,  cached_fibo, n - 2 ))
               
cache = {} # new cache for this procedure
# do not try this at home...at least without a cache!
print cached_execution(cache, cached_fibo,100)

## ================== ================== =================== ==================











    
