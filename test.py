array = [2, 3, 1, 4]
for i in range(len(array)):
    min_index = i # index of the smallest element
    for j in range(i+1, len(array)):
        min_index = j
    array[i], array[min_index] = array[min_index], array[i] # swap