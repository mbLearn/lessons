import random

def poker(hands):
    "Return a list of winning hands: poker([hand,...]) => [hand,...]"
    return allmax(hands, key=hand_rank)

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


mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

def deal(numhands, n=5, deck=mydeck):
    random.shuffle(mydeck)
    return [[mydeck.pop() for n in range(n)] for h in range(numhands)]

##def deal(numhands, n=5, deck=mydeck):
##    new_deck = deck[:]
##    random.shuffle(new_deck)
##    new_numhands = []
##    
##    for x in range(numhands):
##        one_hand = []
##        for i in range(n):
##            card = new_deck.pop()
##            one_hand.append(card)
##        new_numhands.append(one_hand)
##    return new_numhands

##def deal(numhands, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
##    random.shuffle(deck)
##    return[deck[n*i:n*(i+1)] for i in range(numhands)]

        

def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand) 
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)
def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def kind(n, ranks):
    """Return the first rank that this hand has exactly n-of-a-kind of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks


sf1 = "6C 7C 8C 9C TC".split() # Straight Flush
sf2 = "6D 7D 8D 9D TD".split() # Straight Flush
fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
fh = "TD TC TH 7C 7D".split() # Full House
# poker([sf1, sf2, fk, fh]) == [sf1, sf2]
print poker([sf1, sf2, fk, fh]) 
    
