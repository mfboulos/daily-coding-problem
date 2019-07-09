# Problem 1 - Any Two Summed to k

![language](https://img.shields.io/badge/java-1.8-purple.svg?cacheSeconds=2592000)

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

## Specs

### Input

For the sake of simplicity, we'll assume our inputs are integers, but the same logic holds for all numbers, we would just have to account for floating point accuracy.

- List of Integers `nums`
- Integer `k`

### Output

`true` if there exists a pair of numbers a, b in `nums` such that a + b = k, `false` otherwise.

## Timing

#### Start time: 12:13AM
<!--- Work happens here --->
#### End time: 1:08AM

## Runtime Complexity

<img src="https://latex.codecogs.com/gif.latex?\cancel{O\left(n^2\right)}\rightarrow%20O\left(nlogn\right)" />

## Thoughts
First I wanted to go with a brute force solution, which was technically a single pass through `nums`, but since a separate data structure was iterated through that grew with each iteration in `nums`, it felt too slow.

I figured the logic could be refined to `for each num in nums, check if its additive complement with respect to k is in nums`. That improved the runtime to nlogn, as opposed to n<sup>2</sup>.

There is a bit more optimization that I haven't addressed yet: we don't have to binary search through the entire list. We just need the subList of values larger than `num`, because we will have already found any such pair starting with the lower number since we're sorting first and iterating in ascending order. We can also stop iterating once we reach `num/2` by the same logic.

And now that I think about it, why not just have 2 pointers each at the start and end of the list? Increment the lower one if the sum is too small, decrement the upper one if the sum is too big, return false if they meet at the same index. Now that's an idea. Same time complexity for the sort, but it would reduce the algorithm to a single pass. __n time achieved.__

How this can be done in a legitimate single pass without sorting escapes me though. Is n time possible? I don't think so; no reference to ordering makes this a tough egg to crack. We'd still have to brute force it without any natural ordering because searching through unordered data is average n time, which we would have to do for each `num`.
