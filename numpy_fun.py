import numpy as np

# Array Creation
print("Array Creation:")
a = np.array([1, 2, 3])
print("1D array:", a)
b = np.array([[1, 2], [3, 4]])
print("2D array:\n", b)
c = np.zeros((2, 2))
print("Array of zeros:\n", c)
d = np.ones((3, 3))
print("Array of ones:\n", d)
e = np.full((2, 2), 7)
print("Array with all elements as 7:\n", e)
f = np.eye(3)
print("Identity matrix:\n", f)
g = np.random.random((2, 2))
print("Array with random values:\n", g)
h = np.arange(10)
print("Array with range 0 to 9:", h)
i = np.linspace(0, 1, 5)
print("Array with 5 values from 0 to 1:", i)

# Reshape and Transpose
print("\nReshape and Transpose:")
reshaped = h.reshape(2, 5)
print("Reshaped array:\n", reshaped)
transposed = b.T
print("Transposed array:\n", transposed)

# Array Operations
print("\nArray Operations:")
x = np.array([1, 2, 3, 4])
y = np.array([5, 6, 7, 8])
print("x + y:", x + y)
print("x - y:", x - y)
print("x * y:", x * y)
print("x / y:", x / y)
print("x squared:", x ** 2)
print("Sin of x:", np.sin(x))
print("Cos of y:", np.cos(y))
print("Exponential of x:", np.exp(x))
print("Logarithm of y:", np.log(y))

# Aggregate Functions
print("\nAggregate Functions:")
print("Sum of x:", np.sum(x))
print("Minimum of y:", np.min(y))
print("Maximum of y:", np.max(y))
print("Mean of x:", np.mean(x))
print("Standard deviation of x:", np.std(x))

# Indexing and Slicing
print("\nIndexing and Slicing:")
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original Array:\n", arr)
print("Element at (1, 1):", arr[1, 1])
print("Row 0:", arr[0])
print("Column 1:", arr[:, 1])
print("Subarray from (1,1) to (2,2):\n", arr[1:3, 1:3])

# Broadcasting
print("\nBroadcasting:")
broadcasted_sum = arr + 10
print("Array after broadcasting with +10:\n", broadcasted_sum)

# Linear Algebra
print("\nLinear Algebra:")
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
print("Matrix A:\n", matrix_a)
print("Matrix B:\n", matrix_b)
print("Matrix Multiplication:\n", np.dot(matrix_a, matrix_b))
print("Matrix Inverse of A:\n", np.linalg.inv(matrix_a))
print("Determinant of A:", np.linalg.det(matrix_a))
print("Eigenvalues of A:", np.linalg.eig(matrix_a)[0])

# Random Functions
print("\nRandom Functions:")
random_array = np.random.rand(2, 2)
print("Random array with values between 0 and 1:\n", random_array)
random_int_array = np.random.randint(10, 20, (3, 3))
print("Random integer array between 10 and 20:\n", random_int_array)

# Statistical Functions
print("\nStatistical Functions:")
data = np.array([1, 2, 2, 3, 4, 4, 4, 5])
print("Data array:", data)
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Variance:", np.var(data))

# Sorting
print("\nSorting:")
sorted_data = np.sort(data)
print("Sorted array:", sorted_data)
sorted_indices = np.argsort(data)
print("Indices of sorted elements:", sorted_indices)

# Copying and Views
print("\nCopying and Views:")
copy_arr = arr.copy()
view_arr = arr.view()
copy_arr[0, 0] = 99
view_arr[0, 0] = 88
print("Original Array:\n", arr)
print("Copy (independent):\n", copy_arr)
print("View (linked):\n", view_arr)
