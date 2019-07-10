def process_nums(nums):
    # zeroes mess everything up for division, identify them first
    zeroes = nums.count(0)

    # if we have 2 or more zeroes, everything ends up being 0
    if zeroes > 1:
        return [0]*len(nums)
    else:
        nonzero_product = 1
        for num in [n for n in nums if n]:
            nonzero_product *= num
        
        # if we have 1 zero, everything ends up 0 except the value at its index
        if zeroes is 1:
            return [0 if num else int(nonzero_product) for num in nums]
        # otherwise, there are no zeroes, and we can divide!
        else:
            return [int(nonzero_product/num) for num in nums]

# same thing, just can't use division here
# should return the same thing as process_nums(nums) for nonzero integers
def process_nums_no_division(nums):
    return [int(product_others(nums, i)) for i in range(len(nums))]

def product_others(nums, idx):
    # multiply all other nums that aren't the one at idx
    product = 1
    for i, num in enumerate(nums):
        if i is not idx:
            product *= num
    
    return product

assert process_nums([1,2,3,4,5]) == [120, 60, 40, 30, 24]
assert process_nums_no_division([1,2,3,4,5]) == [120, 60, 40, 30, 24]