# Problem 2 - Product Others

![language](https://img.shields.io/badge/python-3.7.3-orange.svg?cacheSeconds=2592000)

Given an array of integers, return a new array such that each element at index `i` of the new array is the product of all the numbers in the original array except the one at `i`.

For example, if our input was `[1, 2, 3, 4, 5]`, the expected output would be `[120, 60, 40, 30, 24]`. If our input was `[3, 2, 1]`, the expected output would be `[2, 3, 6]`.

Follow-up: what if you can't use division?

## Specs

### Input

Array of integers `nums`

### Output

New array of integers `outNums` such that `outNums[i]` is the product of all integers in `nums` except `nums[i]`

## Timing

#### Start time: 2:20PM
<!--- Work happens here --->
#### End time: 3:14PM

## Runtime Complexity

<img src="https://latex.codecogs.com/gif.latex?with%20division-O\left(n\right)" />
<img src="https://latex.codecogs.com/gif.latex?without%20division-O\left(n^2\right)" />

## Thoughts

It was very easy to come up with the solution that the problem then threw away from me immediately; take the product of everything, divide by the single item we don't want. For any __[a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub>]__, the result would be __[a<sub>2</sub>a<sub>3</sub>...a<sub>n</sub>, a<sub>1</sub>a<sub>3</sub>...a<sub>n</sub>, ..., a<sub>1</sub>a<sub>2</sub>...a<sub>n-1</sub>]__, and each element is easily __a<sub>1</sub>a<sub>2</sub>...a<sub>n</sub>/a<sub>i</sub>__ for each `i`. That was __n__ time, pretty easily.

But then we had the light taken away, and my initial reaction was a brute force _multiply everything else for each i_ kind of approach, which quickly hit an upper bound of __n<sup>2</sup>__ time.

I took a while to consider any way we can make that faster, but then I revisited a certain idea; why avoid division if we already have an __n__ time algorithm?

#### Because 0 is an integer

So I realized there were 3 cases.

 1. If there are `2` or more zeroes, the result is a list of `n` zeroes.
 2. If there is `1` zero, the only resulting value is at its index, and everything else zeroes out.
 3. If there are no zeroes, _we can divide without worries_!

So, I refactored the previous __n__ time solution to first count the number of zeroes, then process whatever case was relevant. It maintained __n__ time, and allowed the division solution to persist without edge cases.

Upon researching the solution, I realize I could have gotten the intended division-less __n__ time solution with a visualization. Maybe I should keep a pencil and paper handy next time.