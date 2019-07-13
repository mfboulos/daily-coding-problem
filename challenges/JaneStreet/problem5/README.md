# Pair Construction

![language](https://img.shields.io/badge/python-3.7.3-orange.svg?cacheSeconds=2592000)

`cons(a, b)` constructs a pair, and `car(pair)` and `cdr(pair)` returns the first and last element of that pair. For example, `car(cons(3, 4))` returns `3`, and `cdr(cons(3, 4))` returns `4`.

Given this implementation of cons:

```python
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
```

Implement `car` and `cdr`.

## Specs

### Input

`car` - `pair` constructed by `cons`

`cdr` - `pair` constructed by `cons`

### Output

`car` - first element of `pair`

`cdr` - last element of `pair`

## Timing

#### Start time: 1:11PM
<!--- Work happens here --->
#### End time: 1:18PM

## Runtime Complexity

<img src="https://latex.codecogs.com/gif.latex?\O\left(1\right)" />

## Thoughts

This one was very quick and easy.

`cons(a, b)` returns a method reference that takes a method invoked on `a` and `b`. So basically, the goal was to pass in a method to `pair` that spit back `a` and `b` for `car` and `cdr` respectively. Throw in a couple simple lambdas and it's done.