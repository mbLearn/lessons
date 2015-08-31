## ==================== Problem 1 ======================================
# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.

def symmetric(lst):
    for row in lst:
        if len(row) != len(lst): return False
    column_lst = []
    for i in range(len(lst)):
        new_lst = []
        for m in lst:
            new_lst.append(m[i])
        column_lst.append(new_lst)
    if column_lst == lst : return True
    else: return False

print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]])

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]])

print symmetric([[1, 2],
                [2, 1]])

print symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]])

print symmetric([[1,2,3],
                 [2,3,1]])


## ===================== Alternate solution ==============================
def symmetric1(lst):
    for x in (lst):
        if len(lst) != len(x): return False
    for i, line in enumerate(lst):
	        for j in range(len(line)):
	            if lst[i][j] != lst[j][i]:
	                return False
    return True
