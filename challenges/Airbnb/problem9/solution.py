def largest_sum(nums):
    # let's just iterate through nums and keep a running max to decide
    # for each num, include or exclude?

    inc = 0 # running max sum including previous num
    exc = 0 # running max sum excluding previous num

    for num in nums:
        max_sum = max([inc, exc])
        
        # if we include num, we add to the max sum excluding the previous num
        inc = num + exc
        # if we exclude num, exc becomes the max attainable sum up to the previous num
        exc = max_sum
    
    return max(inc, exc)

assert largest_sum([2, -1, -5, -43, 0, 4, 6, 2, 5]) is 13
assert largest_sum([5, 1, 1, 5]) is 10