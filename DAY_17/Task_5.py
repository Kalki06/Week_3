def capitalize_word(input_string):
    result = ""

    for i in range(len(input_string)):
        if(i==0 or input_string[i-1] == " "):
            result = result + input_string[i].upper()

        else:
            result = result + input_string[i]
    return result

result1 = capitalize_word("hello world")
print(result1)