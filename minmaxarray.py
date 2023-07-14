def sum_of_max_and_min(array):
    if len(array) == 0:
        return 0
    minimum = float('inf')
    maximum = float('-inf')
    for num in array:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
    return minimum + maximum
array = list(map(int, input().split()))
result = sum_of_max_and_min(array)
print(result)
