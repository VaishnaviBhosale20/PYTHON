import array as arr


array1 = arr.array('i', [1, 2, 3, 4, 5])
array2 = arr.array('i', [6, 7, 8, 9, 10])

print("Array1:", array1)
print("Array1:", array2)

print(" Element at index 2 in Array1:", array1[2])
print(" Last element of Array1:", array1[-1])
print("Slice of Array1 (from index 1 to 3):", array1[1:4])

array1.append(6)
print(" Array1 after appending 6:", array1)
array1.extend(array2)
print(" Array1 after extending with Array2:", array1)
array1.insert(1, 100)
print("Array1 after inserting 100 at index 1:", array1)

#Removing an element from an array
array1.remove(100)
print(" Array1 after removing 100:", array1)
popped_element = array1.pop()
print("Array1 after popping an element:", array1, "\nPopped element:", popped_element)

#Finding the index
print("Index of element 3 in Array1:", array1.index(3))

# Counting occurrences
print(" Count of 2 in Array1:", array1.count(2))

array1.reverse()
print("Reversed Array1:", array1)

#Sorting an array
array1_list = list(array1)
array1_list.sort()
array1 = arr.array('i', array1_list)
print("Sorted Array1:", array1)

#Length of an array
print("14. Length of Array1:", len(array1))

# maximum value 
print(" Maximum value in Array1:", max(array1))

#minimum value
print(" Minimum value in Array1:", min(array1))

# Converting array to a list
list_from_array = array1.tolist()
print("List from Array1:", list_from_array)

# Converting a list to an array
new_list = [20, 30, 40]
array_from_list = arr.array('i', new_list)
print(" Array from list:", array_from_list)

# OUTPUT:-
# Array1: array('i', [1, 2, 3, 4, 5])
# Array1: array('i', [6, 7, 8, 9, 10])
#  Element at index 2 in Array1: 3
#  Last element of Array1: 5
# Slice of Array1 (from index 1 to 3): array('i', [2, 3, 4])
#  Array1 after appending 6: array('i', [1, 2, 3, 4, 5, 6])
#  Array1 after extending with Array2: array('i', [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10])
# Array1 after inserting 100 at index 1: array('i', [1, 100, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10])
#  Array1 after removing 100: array('i', [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10])
# Array1 after popping an element: array('i', [1, 2, 3, 4, 5, 6, 6, 7, 8, 9]) 
# Popped element: 10
# Index of element 3 in Array1: 2
#  Count of 2 in Array1: 1
# Reversed Array1: array('i', [9, 8, 7, 6, 6, 5, 4, 3, 2, 1])
# Sorted Array1: array('i', [1, 2, 3, 4, 5, 6, 6, 7, 8, 9])
# 14. Length of Array1: 10
#  Maximum value in Array1: 9
#  Minimum value in Array1: 1
# List from Array1: [1, 2, 3, 4, 5, 6, 6, 7, 8, 9]
#  Array from list: array('i', [20, 30, 40])