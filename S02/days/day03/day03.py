# ===== DAY 03 - NUMPY PRACTICE =====
# numpy is a library for working with arrays (like lists but faster and more powerful)
# we import it as "np" by convention

import numpy as np


# ===== 1. CREATING ARRAYS =====

# from a python list
my_list = [1, 2, 3, 4, 5]
arr = np.array(my_list)
print(arr)
# [1 2 3 4 5]
print(type(arr))
# <class 'numpy.ndarray'>

# zeros, ones, full - like we saw before
weights = np.zeros((3, 3))
print(weights)
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]

biases = np.ones(5)
print(biases)
# [1. 1. 1. 1. 1.]

image_mask = np.full((2, 4), 200)
print(image_mask)
# [[200 200 200 200]
#  [200 200 200 200]]

# arange: like range() but returns an array
print(np.arange(10))
# [0 1 2 3 4 5 6 7 8 9]
print(np.arange(2, 10, 2))
# [2 4 6 8]

# linspace: evenly spaced numbers (inclusive start and end)
print(np.linspace(0, 1, 5))
# [0.   0.25 0.5  0.75 1.  ]

# random arrays
np.random.seed(42)
print(np.random.rand(3))      # uniform [0, 1)
# [0.37454012 0.95071431 0.73199394]
print(np.random.randn(3))     # normal distribution (mean=0, std=1)
# [0.59865848 1.54428042 -0.2257763 ]
print(np.random.randint(0, 10, size=5))
# [5 0 3 3 7]


# ===== 2. ARRAY ATTRIBUTES =====

arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("shape:", arr2d.shape)
# (2, 3) -> 2 rows, 3 columns
print("ndim:", arr2d.ndim)
# 2 -> 2 dimensions
print("size:", arr2d.size)
# 6 -> total elements
print("dtype:", arr2d.dtype)
# int64 (or int32 on some systems)


# ===== 3. INDEXING AND SLICING =====

arr1d = np.array([10, 20, 30, 40, 50])
print(arr1d[0])      # 10
print(arr1d[-1])     # 50
print(arr1d[1:4])    # [20 30 40]
print(arr1d[:3])     # [10 20 30]
print(arr1d[::2])    # [10 30 50]  (every 2nd element)

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[0, 1])   # 2  (row 0, col 1)
print(arr2d[1, :])   # [4 5 6]  (row 1, all cols)
print(arr2d[:, 2])   # [3 6 9]  (all rows, col 2)
print(arr2d[0:2, 1:3])
# [[2 3]
#  [5 6]]


# ===== 4. MODIFYING ARRAYS (they are MUTABLE) =====

arr1d[0] = 99
print(arr1d)
# [99 20 30 40 50]

arr2d[1, 1] = -1
print(arr2d)
# [[ 1  2  3]
#  [ 4 -1  6]
#  [ 7  8  9]]

# slice assignment
arr1d[1:3] = [200, 300]
print(arr1d)
# [99 200 300 40 50]


# ===== 5. BASIC OPERATIONS =====

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)   # [5 7 9]  element-wise addition
print(a - b)   # [-3 -3 -3]
print(a * b)   # [4 10 18]  element-wise multiplication
print(a / b)   # [0.25 0.4  0.5  ]
print(a ** 2)  # [1 4 9]  power
print(a > 2)   # [False False True]  boolean array


# ===== 6. AGGREGATION FUNCTIONS =====

data = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print("sum:", data.sum())       # 31
print("mean:", data.mean())     # 3.875
print("max:", data.max())       # 9
print("min:", data.min())       # 1
print("std:", data.std())       # ~2.75

data2d = np.array([[1, 2], [3, 4]])
print("sum axis=0:", data2d.sum(axis=0))  # [4 6]  column sums
print("sum axis=1:", data2d.sum(axis=1))  # [3 7]  row sums


# ===== 7. BROADCASTING =====
# operations between arrays of different shapes that are compatible

matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([10, 20, 30])
print(matrix + vector)
# [[11 22 33]
#  [14 25 36]]
# the vector is "broadcast" across each row


# ===== 8. BOOLEAN INDEXING =====

scores = np.array([55, 82, 90, 45, 78, 60])
print(scores >= 60)
# [False  True  True False  True  True]
passing = scores[scores >= 60]
print(passing)
# [82 90 78 60]

# replace values with a condition
scores[scores < 60] = 0
print(scores)
# [ 0 82 90  0 78 60]


# ===== 9. RESHAPING =====

flat = np.arange(12)
print(flat)
# [ 0  1  2  3  4  5  6  7  8  9 10 11]

matrix = flat.reshape(3, 4)
print(matrix)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# -1 means "figure out this dimension"
print(flat.reshape(2, -1))
# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]]

# flatten back to 1d
print(matrix.ravel())
# [ 0  1  2  3  4  5  6  7  8  9 10 11]


# ===== 10. COPY VS VIEW =====

original = np.array([1, 2, 3])
view = original[:2]        # slice is a VIEW (shares memory)
copy = original.copy()     # .copy() is a DEEP COPY

view[0] = 99
print("original after view change:", original)  # [99 2 3]

copy[0] = 0
print("original after copy change:", original)  # [99 2 3] (unchanged)


# ===== 11. SAVING AND LOADING ARRAYS =====

# save as .npy (binary, fast, preserves shape/dtype)
data = np.array([[1, 2, 3], [4, 5, 6]])
np.save("my_data.npy", data)
loaded = np.load("my_data.npy")
print(loaded)
# [[1 2 3]
#  [4 5 6]]

# save multiple arrays in .npz
np.savez("multi.npz", a=data, b=np.array([10, 20]))
multi = np.load("multi.npz")
print(multi["a"])
print(multi["b"])
multi.close()  # close the NpzFile to release the handle

# save as text (human readable, slower)
np.savetxt("data.txt", data, delimiter=",", fmt="%d")
txt_data = np.loadtxt("data.txt", delimiter=",")
print(txt_data)


# ===== 12. PRACTICAL EXAMPLE: GRADE ANALYSIS =====
# like the exercises in day04 but with numpy

grades = np.array([
    [14.5, 16.0, 12.5],   # student 1: math, physics, chem
    [10.0, 13.5, 11.0],   # student 2
    [18.0, 17.5, 16.0],   # student 3
    [9.5,  8.0,  10.5],   # student 4
])

print("All grades:")
print(grades)

# average per student (axis=1 = across columns)
student_avg = grades.mean(axis=1)
print("Student averages:", student_avg)

# average per subject (axis=0 = across rows)
subject_avg = grades.mean(axis=0)
print("Subject averages:", subject_avg)

# who passed all subjects (>= 10 in every subject)?
passed = np.all(grades >= 10, axis=1)
print("Passed all:", passed)
# [ True  True  True False]

# count how many passed
print("Number passed:", passed.sum())

# save results
results = np.column_stack((grades, student_avg))
np.savetxt("student_results.csv", results, delimiter=",", header="Math,Physics,Chem,Average", fmt="%.1f")


# ===== SUMMARY =====
# | Task | Code |
# |---|---|
# | Create array | np.array([1,2,3]) |
# | Zeros / ones | np.zeros((2,3)), np.ones(5) |
# | Range | np.arange(0, 10, 2) |
# | Random | np.random.rand(3), np.random.randint(0,10,5) |
# | Shape info | arr.shape, arr.ndim, arr.dtype |
# | Index / slice | arr[0], arr[1:4], arr[0:2, 1:3] |
# | Modify | arr[0] = 5, arr[1:3] = [10,20] |
# | Math ops | a + b, a * 2, a ** 2 |
# | Aggregations | arr.sum(), arr.mean(), arr.max() |
# | Boolean mask | arr[arr > 5] |
# | Reshape | arr.reshape(2, -1) |
# | Save/Load | np.save/load, np.savetxt/loadtxt |


# cleanup demo files (optional)
import os
for f in ["my_data.npy", "multi.npz", "data.txt", "student_results.csv"]:
    if os.path.exists(f):
        os.remove(f)