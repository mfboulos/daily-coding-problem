# Unival Trees

![language](https://img.shields.io/badge/python-3.7.3-orange.svg?cacheSeconds=2592000)

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

```
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
```

## Specs

### Input

Root node `root` to a binary tree

### Output

Number of unival subtrees in the binary tree

## Timing

#### Start time: 6:30PM
<!--- Work happens here --->
#### End time: 7:26PM

## Runtime Complexity

<img src="https://latex.codecogs.com/gif.latex?\cancel{O\left(nlogn\right)}\rightarrow%20O\left(n\right)" />

## Thoughts

Brute forcing this one was pretty easy. Set up a way for the `Node` class I made to figure out if it was unival, then call it for each `Node` recursively. If it is unival, count up all the nodes because _each node of a unival tree is itself the root of a unival subtree_. Return the count, profit.

However, what I noticed is that the complexity needed work. If I am checking "univalness" of each node, then I keep recursively checking the same nodes all the way down. A simpler way to view it is that, if a subtree is non-unival, then the tree as a whole can't be. And non-univalness is _much_ easier to check!

The logical negation of a _for all x, p_ statement is _there exists x such that ~p_. So, really we don't want to accumulate _every single value_ in recursion, we just want to call it non-unival if we find a value that _differs_ from it! In this way, if our recursion works its way _up_ instead of _down_, we won't have to revisit any nodes.

So, I repurposed `Node.is_unival()` to accomplish this, because it was already similarly dependent on its childrens' univalness to return anything. That reduced the average case of __nlogn__ down to __n__.