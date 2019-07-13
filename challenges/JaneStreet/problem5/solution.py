def cons(a, b):
    """
    Returns a pair by returning a method reference on a, b
    """
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    return pair(lambda a, b: a)

def cdr(pair):
    return pair(lambda a, b: b)

pair = cons(3, 4)
assert car(pair) is 3
assert cdr(pair) is 4

pair = cons('123', 0.01)
assert car(pair) is '123'
assert cdr(pair) is 0.01