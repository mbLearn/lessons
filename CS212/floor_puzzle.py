#------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on 
# different floors of a five-floor apartment building. 
#
# Hopper does not live on the top floor. 
# Kay does not live on the bottom floor. 
# Liskov does not live on either the top or the bottom floor. 
# Perlis lives on a higher floor than does Kay. 
# Ritchie does not live on a floor adjacent to Liskov's. 
# Liskov does not live on a floor adjacent to Kay's. 
# 
# Where does everyone live?  
# 
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay, 
# Liskov, Perlis, and Ritchie.

import itertools

def floor_puzzle():
    floors = [bottom, _, _, _, top] = [1,2,3,4,5]
    order = list(itertools.permutations(floors))

    def not_adjcent(no1, no2):
        return abs(no1 - no2) > 1

    def on_top(no1, no2):
        return no1 > no2
    
    return next([Hopper, Kay, Liskov, Perlis, Ritchie]
            for (Hopper, Kay, Liskov, Perlis, Ritchie) in order
            if not_adjcent(Liskov, Kay)
            if not_adjcent(Ritchie, Liskov)
            if on_top(Perlis, Kay)
            if Liskov != 1
            if Liskov != 5
            if Hopper != 5
            if Kay != 1
            )

print floor_puzzle()


## ALternative

def floor_puzzle1():
    floors = bottom,_,_,_,top = [1,2,3,4,5]
    order = list(itertools.permutations(floors))
    for (Hopper, Kay, Liskov, Perlis, Ritchie) in order:
        if (Hopper is not top
            and Kay is not bottom
            and Liskov is not top
            and Liskov is not bottom
            and Perlis > Kay
            and abs(Ritchie - Liskov) > 1
            and abs(Liskov - Kay) > 1):
            return [Hopper, Kay, Liskov, Perlis, Ritchie]

print floor_puzzle1()
