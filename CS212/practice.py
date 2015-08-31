# -----------
# User Instructions
# 
# Define two functions, straight(ranks) and flush(hand).
# Keep in mind that ranks will be ordered from largest
# to smallest.

def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return ranks

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    x = range(ranks[-1], ranks[0]+1)
    x.sort(reverse=True)
    if ranks == x:
        return True
    else:
        return False

def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r,s in hand]
    print suits
    if suits[0] == suits[1] == suits[2] == suits[3] == suits[4]:
        return True
    else: 
        return False
    
##Professor's solution:      
##def straight(ranks):
##    """ Return True if the ordered ranks form a 5-card straight."""
##    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5
##
##def flush(hand):
##    """Return True if all the cards have the same suit. """
##    suits = [s for r,s in hand]
##    return len(set(suits)) == 1


## Alternative recursive solution
##def straight1(ranks):
##    return [True if len(ranks) == 1 else straight(ranks[1:]) if ranks[0]-ranks[1] == 1 else False]
##
##def flush1(hand):
##    return [True if len(hand)== 1 else flush(hand[1:]) if hand[0][1] == hand[1][1] else False]


def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r 
    return None
    
def test():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    tk = "TH QH QC TS 2S".split()
    fkranks = card_ranks(fk)
    tkranks = card_ranks(tk)
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(sf) == True
    assert flush(fk) == False
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
##    assert straight1([9, 8, 7, 6, 5]) == True
##    assert straight1([9, 8, 8, 6, 5]) == False
##    assert flush1(sf) == True
##    assert flush1(fk) == False
    return 'tests pass'

tk = "TH QH QC TS 2S".split()
tkranks = card_ranks(tk)
print test()
print kind(2, tkranks)
