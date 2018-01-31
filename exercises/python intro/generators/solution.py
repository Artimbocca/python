# Write an infinite generator of fibonacci numbers, with optional start values
def fibonacci(a=0, b=1):
    """Fibonacci numbers generator"""
    while True:
        yield a
        a, b = b, a + b


# Write a generator of all permutations of a sequence
def permutations(items):
    n = len(items)
    if n == 0:
        yield []
    else:
        for i in range(len(items)):
            for cc in permutations(items[:i]+items[i+1:]):
                yield [items[i]]+cc


# Use this to write a generator of all permutations of a word
def w_perm(w):
    for wp in permutations(w):
        yield "".join(wp)


# Use the Fibonacci generator to create another one that only generates fib numbers with a given factor
def fib_div(d):
    for f in fibonacci():
        if f % d == 0:
            yield f


def fib_div(d):
    for f in fibonacci():
        if f % d == 0:
            yield f


# Write generator that puts a user-specified limit on the number of items generated by any given generator
def first(n, g):
    for i in range(n):
        yield next(g)


if __name__ == "__main__":
    #f = fibonacci()
    #print(*(next(f) for i in range(10)))
    print(*first(10, (f for f in fibonacci(5,1) if f % 2 == 0)))
    print(*permutations(['r', 'e', 'd']))
    print(*w_perm('game'))

    print(["".join(p) for p in permutations("word")])
