def frequrncy_counter(input_string):
    feq = {}
    words = input_string.split()

    for word in words:
        if word in feq:
            feq[word] += 1
        else:
            feq[word] = 1

    max_repeat = max(feq.values())

    for key, value in feq.items():
        if value == max_repeat:
            return key, max_repeat

string = "Hello world my name is world you are my friend"
result, result1 = frequrncy_counter(string)
print(result , result1)