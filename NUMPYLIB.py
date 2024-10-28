# NUMPY
import numpy as np 
# CREATING 1D ARRAY 
arr1 = np.array([1,2,3,4,5,6,7,8,9,10])
print("ARRAY :- ")
print(arr1)

# SLICING
print("array slicing  5 to 9 :- ",arr1[5:9])
print("array slicing  1 to 5 :- ",arr1[1:5])
print("array slicing  1 to 10 :- ",arr1[1:10])
print("\n\n\n")

# CREATING 2D ARRAY
arr2 = np.array([[1,2,3,4,5,6],[11,12,13,14,15,16],[21,22,23,24,25,26]])
print("2D ARRAY :- \n",arr2)
# 2d array slicing 
print("0th ROW , from 2nd element to 4th element arr2[0,1:4] :- \n",arr2[0,1:4])
print("2nd ROW , from 3rd element to 6th element arr2[2,2:6] :- \n",arr2[2,2:6])
print("\n\n\n")

# COPY function
x=arr1.copy()
x[0]=100
print("Original array :- ",arr1)
print("Copied array :- ",x)
print("\n\n\n")
# view function
y=arr1.view()
y[0]=500
print("original array :-  ",arr1)
print("view array :- ",y)
print("COPY  AND VIEW ARE DIFFERENT IN NUMPY.\nCOPY FUNCTION CREATES A NEW ARRAY WHILE VIEW FUNCTION CREATES A VIEW OF THE ORIGINAL ARRAY.\ncopy function does not  change the original array while view function changes the original array \n \n ")

print("copies own the data,so it will return none:- ",x.base)
print("views does not own the data, so it will return the array :- ",y.base)

# OUTPUT:-
# Drive/Programming/Python/NUMPY/CreatingArray.py
# ARRAY :- 
# [ 1  2  3  4  5  6  7  8  9 10]
# array slicing  5 to 9 :-  [6 7 8 9]
# array slicing  1 to 5 :-  [2 3 4 5]
# array slicing  1 to 10 :-  [ 2  3  4  5  6  7  8  9 10]




# 2D ARRAY :-
#  [[ 1  2  3  4  5  6]
#  [11 12 13 14 15 16]
#  [21 22 23 24 25 26]]
# 0th ROW , from 2nd element to 4th element arr2[0,1:4] :-
#  [2 3 4]
# 2nd ROW , from 3rd element to 6th element arr2[2,2:6] :-
#  [23 24 25 26]




# Original array :-  [ 1  2  3  4  5  6  7  8  9 10]
# Copied array :-  [100   2   3   4   5   6   7   8   9  10]




# original array :-   [500   2   3   4   5   6   7   8   9  10]
# view array :-  [500   2   3   4   5   6   7   8   9  10]
# COPY  AND VIEW ARE DIFFERENT IN NUMPY.
# COPY FUNCTION CREATES A NEW ARRAY WHILE VIEW FUNCTION CREATES A VIEW OF THE ORIGINAL ARRAY.
# copy function does not  change the original array while view function changes the original array


# copies own the data,so it will return none:-  None
# views does not own the data, so it will return the array :-  [500   2   3   4   5   6   7   8   9  10]
# PS C:\Users\vaish\OneDrive\Programming\Python> 