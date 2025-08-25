array = [1, 2, 3, 4, 5]

print("Print Array Elements")
for value in array:
    print(value)

print("Print Array Elements Reversed way")
for i in range(len(array) - 1 , -1, -1):
    print(array[i])

def max_mini():
    array = [23, 45, 12, 56, 78, 34, 65, 32]

    maximum_number = array[0]
    minimum_number = array[0]

    for i in range (len(array)):
        if array[i] < minimum_number:
            minimum_number = array[i]

        if array[i] > maximum_number:
            maximum_number = array[i]

    print("Max number",maximum_number)
    print("Minimum number", minimum_number)

max_mini()