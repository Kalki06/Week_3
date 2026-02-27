l2 = [45, 566, 8954, 834, 58, 239, 923, 2334, 1]

def find_min(numbers):
    min_num = numbers[1]

    for element in numbers:
        if(min_num > element):
            min_num = element
    return min_num

minimum = find_min(l2)
print(minimum)