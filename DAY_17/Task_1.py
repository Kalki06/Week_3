def reverse_string(input_string):
    length = len(input_string) - 1
    reversed_output = ""

    while(length >= 0):
        reversed_output = reversed_output + input_string[length]
        length -= 1

    return reversed_output


string1  = "Manjeet"
result = reverse_string(string1)
print(result)