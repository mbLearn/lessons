import random

def poker(hands):
    """ Return the best hand: poker([hand, ...]) => hand"""
    return allmax(hands, key=hand_rank)

#(example :  max([3,4,5,0]), max([3,4,-5,0], key=abs) here abs is the method
# we are trying to apply on the list. and then find max.

def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    best_hands = []
    max_hand = max(iterable, key=hand_rank)
    for hand in iterable:
        if hand_rank(hand) == hand_rank(max_hand):
                best_hands.append(hand)
    return best_hands

##def allmax1(iterable, key=None):
##    f = key or (lambda x: x) # lambda x maps to x itself. (function to itself). 
##    max_item = max(iterable, f)
##    return [x for x in iterable if f(x) == f(max_item)]
## This is how you use key. This code is same as above but more universal.

def card_ranks(hand):
    """ Return a list of the ranks, sorted with higher first. """
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]  # mapping by index no. 
    ranks.sort(reverse=True)
    return ranks

##def card_ranks_alternative(cards):
##    """ Return a list of the ranks, sorted with higher first. """
##    char_mapping = {'T':10, 'J':11. 'Q':12, 'K':13, 'A':14}
##    ranks = [(cahr_mapping[r] if r in char_mapping else int(r) for r,s in cards)]
##    ranks.sort(reverse=True)
##    return ranks

def straight(ranks):
    """ Return True if the ordered ranks form a 5-card straight."""
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5

def flush(hand):
    """Return True if all the cards have the same suit. """
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for x in ranks:
        if ranks.count(x) == n:
            return x
    return None

def two_pair(ranks):
    """If there are two pair, return the two ranks as a
       tuple: (highest, lowest): otherwise return None."""
    pair = kind(2,ranks)
    lowpair = kind(2,list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None
    
mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

def deal(numhands, n=5, deck=mydeck):
    random.shuffle(mydeck)
    return [[mydeck.pop() for n in range(n)] for h in range(numhands)]

##def deal(numhands, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
##    random.shuffle(deck)
##    return[deck[n*i:n*(i+1)] for i in range(numhands)]



def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, ranks)
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3,ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks), ranks)
    else:                                          # high card
        return (0, ranks)



# Modify the test() function to include two new test cases:
# 1) four of a kind (fk) vs. full house (fh) returns fk.
# 2) full house (fh) vs. full house (fh) returns fh.
def test():
    """Test cases for the funtions in poker program."""
    sf = "6C 7C 8C 9C TC".split()   #straight flush
    fk = "9D 9H 9S 9C 7D".split()   #four of a kind
    fh = "TD TC TH 7C 7D".split()   #full house
    tp = "5S 5D 9H 9C 6S".split()   #two pair
    s1 = "AS 2S 3S 4S 6C".split()   #A-5 straight
    s2 = "2C 3C 4C 5S 6S".split()   #2-6 straight
    ah = "AS 2S 3S 4S 6C".split()   #A high
    sh = "2S 3S 4S 6C 7D".split()   #7 high
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    assert straight([9,8,7,6,5]) == True
    assert straight([9,8,8,7,6]) == False
    assert flush(sf) == True
    assert flush(fk) == False
   # should confirm that fh playing against fh returns fh.
    return "tests pass"

print test()
tp = "5S 5D 9H 9C 6S".split()
print card_ranks(tp)
