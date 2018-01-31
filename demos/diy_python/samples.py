def ffor(it, ivar, block):
    it = iter(it)
    while True:
        try:
            exec("{}={};{}".format(ivar, next(it), block))
        except StopIteration:
            break


class count:
    counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        temp = self.counter
        count.counter += 1
        return temp
