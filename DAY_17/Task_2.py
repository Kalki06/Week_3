def reverse_string(input_string):
    length = len(input_string) - 1
    reversed_output = ""

    while(length >= 0):
        reversed_output = reversed_output + input_string[length]
        length -= 1

    if(reversed_output == input_string):
        return True
    
    return False


string1  = "racecar"
result = reverse_string(string1)
print(result)