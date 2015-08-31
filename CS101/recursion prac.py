## =============================================================
## palindrome -- better solution for longer words or sentences
def iter_palindrome(s):
    for i in range(0, len(s) / 2):
        if s[i] != s[-(i+1)]:
            return False
    return True

## ==============================================================
def sumFirstN(n):
    if n == 0:
        return 0
    else:
        print n
        return sumFirstN(n-1) + n

print sumFirstN(6)


## ==============================================================
## Lucas Number

def lucasNumber(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucasNumber(n-1) + lucasNumber(n-2)

print lucasNumber(7)

## =============================================================
## list binary search

def list_binary_search(my_list, the_value):
    if len(my_list) == 0:
        return False
    elif len(my_list) == 1:
        return my_list[0] == the_value
    else:
        mid_index = len(my_list) // 2
        if the_value < my_list[mid_index]:
            new_list = my_list[ : mid_index]
        else:
            new_list = my_list[mid_index : ]
        return list_binary_search(new_list, the_value)
    

A = [1, 2, 3, 3, 3, 6, 8, 9, 13, 13, 14, 17, 21, 22, 23, 25]
assert( list_binary_search( A, 0) == False )
assert( list_binary_search( A, 1) == True )
assert( list_binary_search( A, 2) == True )
assert( list_binary_search( A, 13) == True )
assert( list_binary_search( A, 24) == False )
assert( list_binary_search( A, 25) == True )
assert( list_binary_search( A, 26) == False )
print("tests of list_binary_search() passed")

##A = [1, 2, 3, 3, 3, 6, 8, 9, 13, 13, 14, 17, 21, 22, 23, 25]
##print list_binary_search( A, 0)
##
##print list_binary_search( A, 13)


## ====================================================================
## list binary search depth

def list_binary_search_depth(my_list, the_value):
    if len(my_list) == 0:
        return [False, 0]
    elif len(my_list) == 1:
        return [my_list[0] == the_value, 0]
    else:
        mid_index = len(my_list) // 2
        if the_value < my_list[mid_index]:
            new_list = my_list[ : mid_index]
        else:
            new_list = my_list[mid_index : ]
        result, depth = list_binary_search_depth(new_list, the_value)
        return [result, depth+1]

A = [1, 2, 3, 3, 3, 6, 8, 9, 13, 13, 14, 17, 21, 22, 23, 25]
assert( list_binary_search_depth( A, 0) == [False, 4] )
assert( list_binary_search_depth( A, 1) == [True, 4] )
assert( list_binary_search_depth( A, 2) == [True, 4] )
assert( list_binary_search_depth( A, 13) == [True, 4] )
assert( list_binary_search_depth( A, 24) == [False, 4] )
assert( list_binary_search_depth( A, 25) == [True, 4] )
assert( list_binary_search_depth( A, 26) == [False, 4] )
print("tests of list_binary_search_depth() passed")


## =====================================================================
## list binary search where

def list_binary_search_where(my_list, the_value, list_first_index = 0):
    if len(my_list) == 0:
        return [False, None]
    elif len(my_list) == 1:
        if my_list[0] == the_value:
            return [True, list_first_index]
        else:
            return [False, None]
    else:
        mid_index = len(my_list) // 2
        if the_value < my_list[mid_index]:
            new_list = my_list[ : mid_index]
            list_first_index = list_first_index + 1
        else:
            new_list = my_list[mid_index : ]
            list_first_index += mid_index
        return list_binary_search_where(new_list, the_value, list_first_index)
       
A = [1, 2, 3, 3, 3, 6, 8, 9, 13, 13, 14, 17, 21, 22, 23, 25]
assert( list_binary_search_where( A, 0) == [False, None] )
assert( list_binary_search_where( A, 1) == [True, 0] )
assert( list_binary_search_where( A, 2) == [True, 1] )
assert( list_binary_search_where( A, 13) == [True, 9] )
assert( list_binary_search_where( A, 24) == [False, None] )
assert( list_binary_search_where( A, 25) == [True, 15] )
assert( list_binary_search_where( A, 26) == [False, None] )
print("tests of list_binary_search_where() passed")
