# Tree Serialization

![language](https://img.shields.io/badge/python-3.7.3-orange.svg?cacheSeconds=2592000)

Given the root to a binary tree, implement `serialize(root)`, which serializes the tree into a string, and `deserialize(s)`, which deserializes the string back into the tree.

For example, given the following `Node` class

```
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

The following test should pass:

```
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
```

## Specs

### Input

`serialize(root)` - root `Node` of a binary tree `root`

`deserialize(s)` - string `s` to deserialize into a binary tree

### Output

`serialize(root)` - string deserialization of the binary tree

`deserialize(s)` - binary tree serialized as `s`

## Timing

#### Start time: 4:30PM
<!--- Work happens here -->
#### End time: 5:19PM

## Runtime Complexity

<img src="https://latex.codecogs.com/gif.latex?serialize%20-%20O\left(n\right)" />
<img src="https://latex.codecogs.com/gif.latex?deserialize%20-%20O\left(n\right)" />

## Thoughts
It took me a while to really figure out how I wanted to serialize this. I was thinking about what kind of rules I wanted to employ, how I would differentiate between the value and the nodes, and I had this weird thing with square brackets in mind that didn't really pan out.

And then I remembered: _serialization already exists_. Why not use JSON?

So I went down that route by converting our `Node`s recursively into `OrderedDict`s to preserve the tree structure and property order. You know, for readability.

I also included a `type` field to get the name of the python object type of `val`, just in case the serialization-deserialization process didn't preserve the type well enough.

And then I thought, what about when we have a non-JSON serializable `val`? Sure, the example use case uses strings, but what about other objects?

So that's when I turned to the ever reliable `pickle` library. The specs were very easily met with that library by changing the `bytes` output to a `str` from `pickle.dumps()` and converting it back to `bytes` for input to `pickle.loads()`. It just loses that human readability that JSON so nicely offers, which is why I was reluctant to start with it, but it also covers _all_ object types, instead of just JSON-serializable types.

Overall, pretty cool problem. I feel the point was to avoid reinventing the wheel.