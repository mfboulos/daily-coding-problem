# Non-Adjacent Sums

![language](https://img.shields.io/badge/python-3.7.3-orange.svg?cacheSeconds=2592000)

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be `0` or negative.

For example, `[2, 4, 6, 2, 5]` should return `13`, since we pick `2`, `6`, and `5`. `[5, 1, 1, 5]` should return `10`, since we pick `5` and `5`.

Follow-up: Can you do this in O(N) time and constant space?

## Specs

### Input

List of integers `nums`

### Output

The largest sum of non-adjacent elements of `nums`

## Timing

#### Start time: 10:58PM
<!--- Work happens here --->
#### End time: 11:52PM

## Runtime Complexity

<img src="https://latex.codecogs.com/gif.latex?time-\cancel{O\left(n^2\right)}\rightarrow%20O\left(n\right)" />
<img src="https://latex.codecogs.com/gif.latex?space-\cancel{O\left(n^2\right)}\rightarrow%20O\left(1\right)" />

## Thoughts

To be honest, this one puzzled me way more than it should've. I really need to start thinking more direct toward process than finding solutions.

My first intuition was to take a look at the first 2 elements. Assuming we take one, remove adjacent elements and call the same function on the remaining slice of the input.

This had many problems. First, and most important, it failed with certain patterns of non-positive numbers. Which would be resolved by filtering them out, but then non-adjacent numbers start to be treated like they're adjacent, and honestly that sucks.

So I filled a piece of paper with a bunch of different examples, which led to a couple other conclusions:
 1. If a number is larger than the sum of its partners, it _must_ be taken.
 2. If no such numbers exist, the largest sum is either the sum of the even or odd indices (not proven to be true, and I don't think it is true anyways)

I managed to put together a more robust process for a solution that would actually work, but it wasn't __n__ time or constant space. And frankly, I just didn't like how weird it was.

So I'm not gonna lie, I cheated here. I went to look for a solution to improve this time and space complexity, but only insofar as the concept, and I left all the writing and implementation to myself.

And really, it showed how much I was overthinking: I completely avoided the route of deciding if single numbers should be included in the sum, just based on how difficult it would be in the scope of the whole list. But what about during an iteration?

The solution I found kept 2 running sums: one representing the maximum attainable sum `incl` _including_ the previous element, and the other representing the maximum attainable sum `excl` _excluding_ the previous element. For each `num`, `incl` would become `excl + num` (since we must exclude the previous element if we're taking `num`) and `excl` would become the max of `incl` and `excl` from the previous element because we want `excl` to be the maximum sum up to that point. At the end, we would just need to get the max of `incl` and `excl` and that would be our answer.

So I slapped myself on the 4head and wrote it out.