import random
import collections 

def factorial(n): return 1 if (n<=1) else n*factorial(n-1)

def swap(deck,i,j):
    "Swap elements i and j of a collection."
    #print 'swap', i,j
    deck[i], deck[j] = deck[j], deck[i]

def  shuffle1(deck):
    "Teacher's Algorithm."
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = random.randrange(N), random.randrange(N)
        swapped[i] = swapped[j] = True
        swap(deck, i , j)
        
def shuffle(deck):
    "Knuth's Algorithm P."
    N = len(deck)
    for i in range(N-1):
        swap(deck, i, random.randrange(N))

def shuffle2(deck):
    "A modification to teacher's Algorithm."
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = random.randrange(N), random.randrange(N)
        swapped[i] = True
        swap(deck, i, j)

def shuffle3(deck):
    "An easier modification of Teacher's Algorithm."
    N = len(deck)
    for i in range(N):
        swap(deck, i, random.randrange(N))
     
    


def test_shuffler(shuffler, deck='abcd', n=10000):
    counts = collections.defaultdict(int)
    for x in range(n):
        input = list(deck)
        shuffler(input)
        counts[''.join(input)] += 1
    e = n*1/factorial(len(deck))
    print e
    ok = all((0.9 <= counts[item]/e <= 1.1) for item in counts)
    name = shuffler.__name__
    print '%s(%s) %s' %(name, deck, ('ok' if ok else '***BAD***'))
    print ' '
    for item, count in sorted(counts.items()):
        print "%s:%4.1f" %(item, count*100/n)
    print


def test_shufflers(shufflers = [shuffle, shuffle1], decks=['abc', 'ab']):
    for deck in decks:
        print
        for f in shufflers:
            test_shuffler(f, deck)




print test_shufflers(shufflers = [shuffle, shuffle1], decks=['abc', 'ab'])  
