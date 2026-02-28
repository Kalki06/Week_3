l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def square_list(numbers):
    squares = []
    for element in numbers:
        square_num = element*element
        squares.append(square_num)
    return squares

print(l2)
result = square_list(l2)
print(result)