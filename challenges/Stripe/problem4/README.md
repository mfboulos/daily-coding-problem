# First Missing Integer

![language](https://img.shields.io/badge/JavaScript-1.7-green.svg?cacheSeconds=2592000)

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input `[3, 4, -1, 1]` should give `2`. The input `[1, 2, 0]` should give `3`.

You can modify the input array in-place.

## Specs

### Input

Array of integers `arr`

### Output

Lowest positive integer not in the array `num`

## Timing

#### Start time: 1:50PM
<!--- Work happens here --->
#### End time: 2:37PM

## Runtime Complexity

<img src="https://latex.codecogs.com/gif.latex?time-O\left(n\right)" />
<img src="https://latex.codecogs.com/gif.latex?space-O\left(1\right)" />

## Thoughts
I like this one! Really made me think about some outside-the-box ways to approach this problem.

I thought I could sort the numbers, then just start at the lowest positive integer and keep a concurrently incrementing value next to it, and return that incrementing value if they're not equal. But sorting is __nlogn__ time, so that fails specs.

I then looked more into the math of the problem, and found out a couple powerful simplifications:

 1. We can ignore _all_ non-positive integers
 2. We can also ignore all integers greater than the length of `arr` because the maximum possible output is given by a permutation of `[1, 2, ..., n]`, which gives `n + 1`, and any modification to a value of `arr` would change the output to the pre-modification value.

Example:
```javascript
let arr = [1, 2, 3, 4]
firstMissingInteger(arr) // 5
let arr2 = [1, 2, 7, 4]
firstMissingInteger(arr2) // 3
```

So I thought of keeping a parallel boolean array `markers` of size `n` that marks the values from `1` to `n` that we encounter, then iterate through `markers`. That would be __n__ time, but also __n__ space which, once again, fails specs.

I then revisited the point at the end of the problem: _you can modify the input array in-place_. Say no more fam.

So I figured I could go through the array in 3 passes. It could have been less, but I kept it in 3 for the sake of clarity:

 1. Set all irrelevant values in `arr` to `false`
 2. For each value in `arr`, if it is a number `num`, set the value at that corresponding index `num-1` to `true`. If there is currently a number `num2` there, set the value at that corresponding index `num2-1` to `true`. Do this recursively.

 The reason this is `n` time is because we are modifying the value at the desired index to `true` before recursing. We only recursively look at the next value if there is a number. We'll never have to revisit that index in the same recursive fashion, but we may have to set an already `true` value to `true` again. That's ok, because that doubles the usual work in the absolute worst case.

 Example:
 ```
 arr = [3, 4, -1, 1]
    => [3, 4, false, 1]
    => [3, 4, true, 1] // saw 3, changed arr[2] to true, didn't recurse
    => [3, 4, true, true] // saw 4, changed arr[3] to true, recursed with 1
    => [true, 4, true, true] // saw 1, changed arr[0] to true, recursed with 3
    => [true, 4, true, true] // saw 3, changed arr[3] to true, didn't recurse
 ```

 3. Iterate through `arr` and return the first `false` or `Number` encountered. If none are found, return `n + 1`.

Although this completely mutilates our original array, we do 3 subequent __n__ time actions, resulting in overall __n__ time, and none of the space allocated is dependent on __n__, so it's also constant space.

Just to kinda delve further, the most efficient way I can think of to maintain the input array and achieve the same result would be to lose the constant space requirement, and use a boolean filter array like I described above. That would maintain __n__ time, and assuming the programming language has a data structure to pack booleans into all bits of a byte, it would use at most `floor(n/8)` bytes of space.