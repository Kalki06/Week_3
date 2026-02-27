def find_max(numbers):
    max_num = 0

    for element in numbers:
        if(element > max_num):
            max_num = element
    
    return max_num

l1 = []

i = 1

while(i<=5):
    user_input = int(input(f"Enter the {i} element in list : "))

    l1.append(user_input)
    i+=1

max_element = find_max(l1)
print(l1)
print(l1[0])
print(l1[4])
print(max_element)
