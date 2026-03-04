def remove_duplicate(input_string):
    unique_string = ""
    lowcase_string = input_string.lower()

    for char in lowcase_string:
        if char not in unique_string:
            unique_string = unique_string + char
    return unique_string

result = remove_duplicate("banana")
print(result)