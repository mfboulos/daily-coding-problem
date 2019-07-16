# Message Encoding

![language](https://img.shields.io/badge/python-3.7.3-orange.svg?cacheSeconds=2592000)

This problem was asked by Facebook.

Given the mapping `a = 1`, `b = 2`, ... `z = 26`, and an encoded message, count the number of ways it can be decoded.

For example, the message `111` would give `3`, since it could be decoded as `aaa`, `ka`, and `ak`.

You can assume that the messages are decodable. For example, `001` is not allowed.

## Specs

### Input

A string `encoded_str` decodable using the above mapping

### Output

Number of ways that `str` can be decoded using the above mapping

## Timing

#### Start time: 1:35AM
<!--- Work happens here --->
#### End time: 2:45AM

## Runtime Complexity

Assuming a mapping of `m` entries and an input string of length `n`:

<img src="https://latex.codecogs.com/gif.latex?\cancel{O\left(nm\right)}\rightarrow%20O\left(nlogm\right)" />

## Thoughts

Initial solution, super easy:

 1. If the starting number is `0`, return `0`. None of our encoded values start with `0`.
 2. If the starting number is `3` or greater, return the number of encodings of the substring of `encoded_str` starting at index `1`. None of our encoded values starting with any of these values have any more than one digit.
 3. if the starting value is `1` or `2`, return the number of encodings of the substring of `encoded_str` starting at index `1`, and if it's at least length 2, sum it with the number of encodings of the substring of `encoded_str` starting at index `2`. We actually have encoded values with two digits that start with `1` and `2`.

But let's be honest, that's super hacky. I mean, we're fortunate the mapping is simple enough to allow this kind of logic. So I didn't even count it.

Instead, let's assume a more general `mapping`. Now we have to replace this logic with something along the lines of "_find the encoded values that `encoded_str` starts with_".

First intuition, just iterate through `mapping.values()`, get all the values out, easy peasy lemon squeezy. But that's linear time. Why can't we do better if we can narrow down the options _per character_?

So I made a 256-ary tree structure instead to store `mapping.values()` (assuming we're only dealing with ASCII value encodings, otherwise that value would change), which stores the existence of encoded values via traversal and flag checking at each node. Basically, if a node has a `True` flag, the traversal up to that point was an actual encoded value.

Anyways, this brought our linear time average case for encoding searches to a much nicer log time with respect to `m`!

And the time complexity for the iteration through the string remained the same. I figured it was linear with respect to `n` based on the logical similarity of the way we recurse on the string to the infamous [Staircase Problem](https://www.dailycodingproblem.com/blog/staircase-problem/).