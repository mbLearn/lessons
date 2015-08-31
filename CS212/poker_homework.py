## Poker Homework1, Problem 1:7-card Stud
import itertools

def best_hand(hand):
    return max([list(e) for e in itertools.combinations(hand,5)], key=hand_rank)

def card_ranks(hand):
    """ Return a list of the ranks, sorted with higher first. """
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]  # mapping by index no. 
    ranks.sort(reverse=True)
    return ranks

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

def test_best_hand():
    assert(sorted(best_hand("6C 7C 8C 9C TC 5C JS".split()))
           == ['6C', '7C', '8C', '9C' , 'TC'])
    assert(sorted(best_hand("TD TC TH 7C 7D 8C 8S".split()))
           == ['8C', '8S', 'TC', 'TD' , 'TH'])
    assert(sorted(best_hand("TD TC TH 7C 7D 7S 7H".split()))
           == ['7C', '7D', '7H', '7S' , 'TD'])
    return 'test_best_hand_passes'

one_hand = "7H TH QH 5C KC 3H 4D 7D".split()
print best_hand(sorted(one_hand))
