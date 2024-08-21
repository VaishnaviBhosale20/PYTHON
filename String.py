# 2 sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}


set1.add(7)
print("After adding 7 to set1:", set1)

set1.remove(2) 
print("After removing 2 from set1:", set1)

set1.discard(10) 
print("After discarding 10 from set1:", set1)

set1.discard(3) 
print("After discarding 10 from set1:", set1)

union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)

difference_set = set1.difference(set2)
print("Difference of set1 and set2:", difference_set)

sym_diff_set = set1.symmetric_difference(set2)
print("Symmetric difference of set1 and set2:", sym_diff_set)

is_subset = set1.issubset(set2)
print("Is set1 a subset of set2? :- \n", is_subset)

is_superset = set1.issuperset(set2)
print("Is set1 a superset of set2? :- \n", is_superset)

new_set = set1.copy()
print("Copy of set1:", new_set)

set1.clear()
print("After clearing set1:- \n", set1)

# OUTPUT:-
# After adding 7 to set1: {1, 2, 3, 4, 7}
# After removing 2 from set1: {1, 3, 4, 7}
# After discarding 10 from set1: {1, 3, 4, 7}
# After discarding 10 from set1: {1, 4, 7}
# Union of set1 and set2: {1, 3, 4, 5, 6, 7}
# Intersection of set1 and set2: {4}
# Difference of set1 and set2: {1, 7}
# Symmetric difference of set1 and set2: {1, 3, 5, 6, 7}
# Is set1 a subset of set2? :-
#  False
# Is set1 a superset of set2? :-
#  False
# Copy of set1: {1, 4, 7}
# After clearing set1:-
#  set()