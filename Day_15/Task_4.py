l2 = [1, 34,45,42,45,324,43234,324,34]

def search_element(numbers, target):
    for element in numbers:
        if element == target:
            return True
    return False

result = search_element(l2, 23)
print(result)
