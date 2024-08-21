#initialize frozenset a and b

a = frozenset([11, 12, 13, 14,23,25])

b = frozenset([23, 24, 25, 26,11,12])

print(a.isdisjoint(b))

print(a.difference(b))

print(a|b)


frozen_set = frozenset([1, 2, 3, 4, 5])
print("Original frozenset:", frozen_set)

print("Is 3 in frozenset?", 3 in frozen_set)
print("Is 6 in frozenset?", 6 in frozen_set)

print("Iterating through frozenset:")
for item in frozen_set:
    print(item)

print("Length of frozenset:", len(frozen_set))

another_frozen_set = frozenset([4, 5, 6, 7])
union_set = frozen_set | another_frozen_set
print("Union of frozensets:", union_set)

intersection_set = frozen_set & another_frozen_set
print("Intersection of frozensets:", intersection_set)

difference_set = frozen_set - another_frozen_set
print("Difference of frozensets:", difference_set)

symmetric_difference_set = frozen_set ^ another_frozen_set
print("Symmetric difference of frozensets:", symmetric_difference_set)

print("subset :- ", frozen_set.issubset(another_frozen_set))

print("superset:- ", frozen_set.issuperset(another_frozen_set))

print("isdisjoint:-", frozen_set.isdisjoint(another_frozen_set))

copyset = frozen_set.copy()
print("Copy of frozenset:", copyset)
