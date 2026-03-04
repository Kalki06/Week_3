def frequency(input_string):
    frq = {}
    low_string = input_string.lower()

    for char in low_string:
        if char in frq:
            frq[char] += 1
        else:
            frq[char] = 1
    return frq

result = frequency("banamaaasnjs")
print(result)