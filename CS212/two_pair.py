def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return ranks



def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    new_x = []
    for x in ranks:
        if ranks.count(x) == 2:
            new_x.append(x)
        new_x.sort(reverse=True)
    return (new_x[0], new_x[2])
    

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r 
    return None

tk = "TH QH QC TS 2S".split()
tkranks = card_ranks(tk)

print two_pair(tkranks)


def two_pair2(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    if kind(2, ranks) and kind(2, ranks[::-1]) and kind(2,ranks) != kind(2, ranks[::-1]):
        return (kind(2, ranks), kind(2, ranks[::-1]))
    else:
        return None
##And that's how it works:
##1) check if there is a pair starting from the highest rank
##2) check if there is a pair starting from the lowest rank
##3) check if the pairs from 1) and 2) are different (so not the same pair found twice)
##If these three conditions are satisfied, we return the tuple with two results.
##Otherwise we return None.

print two_pair2(tkranks)
