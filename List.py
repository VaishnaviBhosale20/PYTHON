my_list = [1,2,3]

my_list.append(6)
print("After appending 6:", my_list)

my_list.extend([7, 8, 9])
print("After extending with [7, 8, 9]:", my_list)

my_list.insert(0, 0)
print("After inserting 0 at index 0:", my_list)

my_list.remove(3)
print("After removing 3:", my_list)

popped_element = my_list.pop()  
print("After popping the last element:", my_list)
print("Popped element:", popped_element)

index = my_list.index(2)
print("Index of 2:", index)

count_of_2 = my_list.count(2)
print("Count of 2:", count_of_2)

my_list.sort()
print("After sorting:", my_list)
my_list.reverse()
print("After reversing:", my_list)

new_list = my_list.copy()
print("Copy of the list:", new_list)

my_list.clear()
print("After clearing the list:", my_list)

numbers = [10, 20, 30, 40, 50]
print("Minimum value in numbers:", min(numbers))
print("Maximum value in numbers:", max(numbers))

print("Sum of numbers:", sum(numbers))

print("Length of numbers:", len(numbers))
# OUTPUT:-
# After appending 6: [1, 2, 3, 6]
# After extending with [7, 8, 9]: [1, 2, 3, 6, 7, 8, 9]
# After inserting 0 at index 0: [0, 1, 2, 3, 6, 7, 8, 9]
# After removing 3: [0, 1, 2, 6, 7, 8, 9]
# After popping the last element: [0, 1, 2, 6, 7, 8]
# Popped element: 9
# Index of 2: 2
# Count of 2: 1
# After sorting: [0, 1, 2, 6, 7, 8]
# After reversing: [8, 7, 6, 2, 1, 0]
# Copy of the list: [8, 7, 6, 2, 1, 0]
# After clearing the list: []
# Minimum value in numbers: 10
# Maximum value in numbers: 50
# Sum of numbers: 150
# Length of numbers: 5