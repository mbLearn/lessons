##Zebra Puzzle
##


##
##2 The Englishman lives in the red house.
##
##3 The Spaniard owns the dog.
##
##4 Coffee is drunk in the green house.
##
##5 The Ukrainian drinks tea.
##
##6 The green house is immediately to the right of the ivory house.
##
##7 The Old Gold smoker owns snails.
##
##8 Kools are smoked in the yellow house.
##
##9 Milk is drunk in the middle house.
##
##10 The Norwegian lives in the first house.
##
##11 The man who smokes Chesterfields lives in the house next to
##   the man with the fox.
##
##12 Kools are smoked in a house next to the house where
##   the horse is kept.
##
##13 The Lucky Strike smoker drinks orange juice.
##
##14 The Japanese smokes Parliaments.
##
##15 The Norwegian lives next to the blue house.
##
##Who drinks water? Who owns the zebra?
##
##Each house is painted a different color, and their inhabitants are
##of different nationalities, own different pets, drink different
##beverages and smoke different brands of American cigarettes.

import itertools
import time

def zebra_puzzle():
    "return a tuple(WATER, ZEBRA) indicating their house numbers."
    houses = [first, _, middle, _, _] = [1,2,3,4,5]
    orderings = list(itertools.permutations(houses))  #1 Rule no. 1
    #print orderings
    solutions =((WATER, ZEBRA, [Englishman, Spaniard, Ukranian, Japanese, Norwegian])
        for (red, green, ivory, yellow, blue) in orderings
        if imright(green, ivory)                      # Rule 6
        for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in c(orderings) # here c() is debugging tool
        if Englishman is red                          # Rule 2
        if Norwegian is first                         # Rule 10
        if nextto(Norwegian, blue)                    # Rule 15
        for (coffee, tea, milk, oj, WATER) in c(orderings)
        if coffee is green                            # Rule 4
        if Ukranian is tea                            # Rule 5
        if milk is middle                             # Rule 9
        for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in c(orderings)
        if Kools is yellow                            # Rule 8
        if LuckyStrike is oj                          # Rule 13
        if Japanese is Parliaments                    # Rule 14
        for (dog, snails, fox, horse, ZEBRA) in c(orderings)
        if Spaniard is dog                            # Rule 3
        if OldGold is snails                          # Rule 
        if nextto(Chesterfields, fox)
        if nextto(Kools, horse)
        )
    water, zebra, people = next(solutions)
    nat = 'Englishman Spaniard Ukranian Japanese Norwegian'.split(' ')
    return (nat[people.index(water)], nat[people.index(zebra)])

def imright(h1, h2):
    "House h1 is immidiately right of h2 if h1-h2 == 1."
    return h1-h2 == 1

def nextto(h1,h2):
    "Two houses are next to each other if they differ by 1."
    return abs(h1-h2) == 1


##def t():
##    t0 = time.clock()
##    zebra_puzzle()
##    t1 = time.clock()
##    return t1 - t0

## better yet

def timedcall(fn):
    "call function and return elapsed time."
    t0 = time.clock()
    fn()
    t1 = time.clock()
    return t1 - t0

def instrument_fn(fn, *args):
    """this function will count the calls that it takes to execute
       the calling of a funtion with the arguments."""
    c.starts, c.items = 0,0
    result = fn(*args)
    print ('%s got %s with %5d iters over %7d items.' %(fn.__name__, result, c.starts, c.items))

# c() keeps track of two counts -- no. of starts , the times we
# started the iterations; strated the for loop, that was measured
# with the c function, and the number of items that we got thru.

def c(sequence):
    """ Generate items in a sequence; keeping counts as we go. c.strats is the
        number of sequences started; c.times is the number of items generated."""
    c.starts += 1
    for item in sequence:
        c.items += 1
        yield item


## What it does is it takes a sequence, it says this is the first time i've been called.
## I'm going to initialize my strats to one. Then I'm going to enter into a loop and this
## means that c is a generator function. The generator funtion will be returned, and as
## part of the protocol, we'll call that generator function each time we want the next item
## in the sequence and each time we do that, our count wof items will be incremented.

print instrument_fn(zebra_puzzle)
