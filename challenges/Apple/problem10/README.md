# Job Scheduler

![language](https://img.shields.io/badge/python-3.7.3-orange.svg?cacheSeconds=2592000)

Implement a job scheduler which takes in a function `f` and an integer `n`, and calls `f` after `n` milliseconds.

## Specs

### Input

Function `f` and integer `n`

### Output

`f` is called after `n` milliseconds

## Timing

#### Start time: 8:55PM
<!--- Work happens here --->
#### End time: 10:10PM

## Runtime Complexity

<img src="https://latex.codecogs.com/gif.latex?N/A" />

## Thoughts

I spent _so much time_ writing a job queue and trying to implement it, but really. Python has a `Timer` module. How did I not think about it?

Timer postpones execution of a function `f` for `s` seconds, so we just needed to make one of those timers, start it, and divide `n` by `1000` to get `s`. Super nice and easy scheduler.