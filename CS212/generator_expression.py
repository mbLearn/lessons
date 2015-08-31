def foo():
    i = 0
    while True:
        yield i
        i += 1


def int_all():
    "Generate integers in the order  0,+1, -1, +2, -2, +3, -3, ....."
    yield 0
    i = 1
    while True:
        yield +i
        yield -i
        i = i + 1

def pi_series():
    sum = 0
    i = 1.0; j = 1
    while(1):
        sum = sum + j/i
        yield 4 * sum
        i = i + 2; j = j * -1


def firstn(g,n):
    "Return the first N values yielded by a generator."
    for i in range(n):
        yield g.next()

print list(firstn(pi_series(), 8))



## Prime numbers

def firstn(g, n):
	for i in range(n):
		yield g.next()

def intsfrom(i):
	while 1:
		yield i
		i = i + 1

def exclude_multiples(n, ints):
	for i in ints:
		if (i % n): yield i

def sieve(ints):
	while 1:
		prime = ints.next()
		yield prime
		ints = exclude_multiples(prime, ints)
	
if __name__ == '__main__':
	for i in firstn(sieve(intsfrom(2)), 400):
		print i

           

