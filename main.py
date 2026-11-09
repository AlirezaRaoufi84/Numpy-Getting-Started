import numpy as np

array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(array.shape)  # [4,4]
print(array.ndim)  # 2
print(array[0, 0])  # 1

print(array[0, 2] + array[2, 2] == array[-1, 1])  # 3 + 11 == 14 => True

# Array range => array[start:stop:step]

print(array[1:4])
"""
[[ 5  6  7  8]
 [ 9 10 11 12]
 [13 14 15 16]]
 """
print(array[-1::-2])
"""
[[13 14 15 16]
 [ 5  6  7  8]]
 """
print(array[:2, :2])
print(array[:2, 2:])

print(array[:, ::2])  # only odd numbers show up
print(array[:, 1::2])  # only evens numbers show up

# Scalar arithmetic

array = np.array([1, 2, 3])

print(array + 5)  # [6 7 8]
print(array * 2)  # [2 4 6]
print(array / 4)  # [0.25 0.5 0.75]
