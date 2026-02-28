nums  = [123, 34, 324, 4545, 567, 13, 6, 57, 24]
nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def check_sort(numbers):
    i = 0
    current_element = numbers[i]
    next_element = numbers[i+1]

    while( i < len(numbers)):
        if(current_element < next_element):
            i+=1
        else:
            return False
            
    return True

result_l1 = check_sort(nums)
print(result_l1)

result_l2 = check_sort(nums1)
print(result_l2)

