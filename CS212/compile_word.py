import re, itertools, string
def faster_solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None.
    This version precompiles the formula; only one eval per formula."""
    f, letters = compile_formula(formula)
    for digits in itertools.permutations((1,2,3,4,5,6,7,8,9,0), len(letters)):
        try :
            if f(*digits) is True:
                table = string.maketrans(letters, ''.join(map(str, digits)))
                return formula.translate(table)
        except ArithmeticError:
            pass

def compile_formula(formula, verbose=False):
    """Compile formula into a function. Also return letters found, as a str,
    in same order as parms of function. For example, 'YOU == ME**2' returns
    (lambda Y,M,E,U,O:(U+10*O+100*Y) == (E+10*M)**2), 'YMEUO' """
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    parms = ', '.join(letters)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    body = ''.join(tokens)
    f = 'lambda %s: %s' %(parms, body)
    if verbose: print f
    return eval(f), letters
    

# User Instructions
#
# Write a function, compile_word(word), that compiles a word
# of UPPERCASE letters as numeric digits. For example:
# compile_word('YOU') => '(1*U + 10*O +100*Y)' 
# Non-uppercase words should remain unchaged.

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    # Your code here.
    if word.isupper():
        term = [('%s*%s' %(10**i, d))
                 for i,d in enumerate(word[::-1])]
        return '(' + ' + '.join(term) + ')'
    else: 
        return word
                
formula = 'YOU == ME**2'
formula1 = 'ODD + ODD == EVEN'
print  faster_solve(formula)
print  faster_solve(formula1)   
#print compile_word('YOU') 
#=> '(1*U + 10*O +100*Y)'


## It reverses a list

## a=[1,2,3,4,5]
## a[::-1]
## [5, 4, 3, 2, 1]
##The slicing notation is: a[start:stop:steps]
##If steps is negative it start counting from -1, ie: from a[-1] to a[0].
##It's equivalent to reverse()

## Yes. I was completely lost. By the wording of the question,
## I didn't understand that we were trying to plug the letters in to
## the formula, so the example # compile_word('YOU') => '(1U + 10O +100*Y)'
## really threw me.(although I guess I should have just followed that example.)
##
##So if you are still trying to figure out your code, DO this:
##Given a word, for example "YOU', return the string '(1U + 10O +100Y)'.
##If the word were 'THEM', you would return '(1M + 10E +100H + 1000*T)'.
##
## I was able to follow the answer once I saw it, although I doubt I
## would have come up with that answer.
## And the reason we are doing this is because something, something
## lamdba something, something. I think.
