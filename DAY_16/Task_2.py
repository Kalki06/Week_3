nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def odd_list(nums):
    odd = []
    for element in nums:
        if element%2 != 0:
            odd.append(element)
    return odd

print(nums)
result = odd_list(nums)
print(result)