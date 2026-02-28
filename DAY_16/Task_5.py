nums  = [123, 34, 324, 4545, 567, 13, 6, 57, 24]
nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def merge_list(num1, num2):
    merged_list = num1

    for element in num2:
        merged_list.append(element)
    
    return merged_list

result = merge_list(nums, nums1)
print(result)