from __future__ import division 
import time, re, itertools, string
import cProfile

examples = """TWO + TWO == FOUR
A**2 + B**2 == C**2
A**2 + BE**2 == BY**2
X / X == X
A**N + B**N == C**N and N > 1
ATOM**0.5 == A + TO + M
GLITTERS is not GOLD
ONE < TWO and FOUR < FIVE
ONE < TWO < THREE
RAMN == R**3 + RM**3 == N**3 + RX**3
sum(range(AA)) == BB
sum(range(POP)) == BOBO
ODD + ODD == EVEN
PLUTO not in set([PLANETS])""".splitlines()

def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    for f in fill_in(formula):
        if valid(f):
            return f

def fill_in(formula):
    "Generate all possible fillings-in of letters in formula with digits."
    letters = ''.join(set(re.findall('[A-Z]', formula))) #should be a string
    for digits in itertools.permutations('1234567890', len(letters)):
        table = string.maketrans(letters, ''.join(digits))
        yield formula.translate(table)

def valid(f):
    """Formula f is valid if and only if it has no
    numbers with leading zero, and evals true."""
    try:
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False
    
def test():
    t0 = time.time()
    for example in examples:
        print; print 13*' ', example
        print '%6.4f sec:   %s ' % timedcall(solve, example)
    print '%6.4f tot.' % (time.time()-t0)


def add (a):
    return a+a

def timedcall(fn, *args):
    "Call function with args; return the time in seconds."
    t0 = time.time()
    result = fn(*args)
    t1 = time.time()
    return t1-t0, result

def timedcalls(n, fn, *args):
    """Call function(*args) repeatedly; n times if n is an int,
    or upto n seconds if n is a float; return the min, avg, max time. """
    if isinstance(n, int):
        times = [timedcall(fn, *args)[0] for _ in range(n)]
    else:
        times = []
        total = 0.0
        while total < n:
            t = timedcall(fn , *args)[0]
            total += t
            times.append(t)
    return min(times), average(times), max(times)

def average(numbers):
    "Return the average (arithmetic mean) of a sequence of numbers."
    return sum(numbers) / float(len(numbers))


cProfile.run('test()')
