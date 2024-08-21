# tuple,array,
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (6, 7, 8, 9, 10)
tuple3 = ('a', 'b', 'c', 'd', 'e')

print("Tuple1:", tuple1)

print("Element at index 2 in Tuple1:", tuple1[2])
print("Last element of Tuple1:", tuple1[-1])

# Slicing :-
print("Sliced Tuple1 (from index 1 to 3):", tuple1[1:4])
#Concatenating 
tuple_concat = tuple1 + tuple2
print("Concatenated Tuple:", tuple_concat)
#Repeating a tuple
tuple_repeated = tuple1 * 2
print(" Repeated Tuple1:", tuple_repeated)

#Checking membership
print("Is 3 in Tuple1?", 3 in tuple1)

#length of a tuple :-
print("Length of Tuple1:", len(tuple1))

# maximum value
print(" Maximum value in Tuple1:", max(tuple1))

#minimum value 
print(" Minimum value in Tuple1:", min(tuple1))

#Counting occurrences of an element
tuple_count = (1, 2, 2, 3, 4, 2)
print(" Count of 2 in Tuple:", tuple_count.count(2))

#Finding the index
print(" Index of element 'c' in Tuple3:", tuple3.index('c'))

#list into a tuple
list1 = [10, 20, 30]
tuple_from_list = tuple(list1)
print("Tuple from list:", tuple_from_list)

# tuple into a list
list_from_tuple = list(tuple1)
print("List from Tuple1:", list_from_tuple)

#Unpacking into variables
a, b, c, d, e = tuple1
print(" Unpacked values from Tuple1:", a, b, c, d, e)

# nested tuple
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(" Nested Tuple:", nested_tuple)

# Accessing element from a nested tuple
print(" Element from Nested Tuple (1st tuple, 2nd element):", nested_tuple[0][1])

#Reversing a tuple
reversed_tuple = tuple(reversed(tuple1))
print(" Reversed Tuple1:", reversed_tuple)

#Sorting a tuple
sorted_tuple = sorted(tuple1)
print("Sorted Tuple1 (as a list):", sorted_tuple)

tuple_to_delete = (10, 20, 30)
print("Tuple before deletion:", tuple_to_delete)
del tuple_to_delete
print("Tuple deleted")


zipped_tuples = zip(tuple1, tuple2)
print("Zipped Tuples:", list(zipped_tuples))


# OUTPUT:- 
#     Tuple1: (1, 2, 3, 4, 5)
# Element at index 2 in Tuple1: 3
# Last element of Tuple1: 5
# Sliced Tuple1 (from index 1 to 3): (2, 3, 4)
# Concatenated Tuple: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#  Repeated Tuple1: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
# Is 3 in Tuple1? True
# Length of Tuple1: 5
#  Maximum value in Tuple1: 5
#  Minimum value in Tuple1: 1
#  Count of 2 in Tuple: 3
#  Index of element 'c' in Tuple3: 2
# Tuple from list: (10, 20, 30)
# List from Tuple1: [1, 2, 3, 4, 5]
#  Unpacked values from Tuple1: 1 2 3 4 5
#  Nested Tuple: ((1, 2), (3, 4), (5, 6))
#  Element from Nested Tuple (1st tuple, 2nd element): 2
#  Reversed Tuple1: (5, 4, 3, 2, 1)
# Sorted Tuple1 (as a list): [1, 2, 3, 4, 5]
# Tuple before deletion: (10, 20, 30)
# Tuple deleted
# Zipped Tuples: [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
# PS C:\Users\vaish\OneDrive\PYTHONPROGRAMS\ASS1>