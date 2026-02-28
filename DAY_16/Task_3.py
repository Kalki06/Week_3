nums = [23, 45, 223,34, 54, 43, 675]

def second_largest_ele(nums):
    largest = 0
    second_largest = 0

    for element in nums:
        if element > largest:
            second_largest = largest
            largest = element
    return second_largest

result = second_largest_ele(nums)
print(result)