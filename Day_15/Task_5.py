l2 = [12, 45, 45, 455, 66, 33, 79]

def remove_element(numbers, target):
    for element in numbers:
        if element == target:
            l2.remove(element)
            return True
    return False

result = remove_element(l2, 455)
print(result)
print(l2)

result2 = remove_element(l2, 1)
print(result2)
print(l2)