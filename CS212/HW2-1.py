import re
import itertools
import string

def compile_formula(formula, verbose=False):
    """Compile formula into a function. Also return letters found, as a str,
    in same order as parms of function. The first digit of a multi-digit 
    number can't be 0. So if YOU is a word in the formula, and the function
    is called with Y eqal to 0, the function should return False."""
    
    # modify the code in this function.
    
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    firstletters = set(re.findall(r'\b([A-Z])[A-Z]', formula))
    print firstletters
    parms = ', '.join(letters)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    body = ''.join(tokens)
    if firstletters:
        tests = ' and '.join(L + '!=0' for L in firstletters)
        body = '%s and (%s)' %(tests, body)
        #print tests
        #print body
    f = 'lambda %s: %s' % (parms, body)
    if verbose: print f
    #print eval(f)
    return eval(f), letters
    

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words uncahanged: compile_word('+') => '+'"""
    if word.isupper():
        terms = [('%s*%s' % (10**i, d)) 
                 for (i, d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
    else:
        return word
    
def faster_solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None.
    This version precompiles the formula; only one eval per formula."""
    f, letters = compile_formula(formula)
    print f, letters
    print
    for digits in itertools.permutations((1,2,3,4,5,6,7,8,9,0), len(letters)):
        try:
            if f(*digits) is True:
                table = string.maketrans(letters, ''.join(map(str, digits)))
                return formula.translate(table)
        except ArithmeticError:
            pass
formula = 'A + B == BA'
formula1 = 'YOU == ME**2'
print compile_formula(formula)
print
print faster_solve(formula)
print

print faster_solve(formula1)
