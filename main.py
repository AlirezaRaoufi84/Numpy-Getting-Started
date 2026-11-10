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

# Vectorize math functions

array = np.array([12, -25, 31])
absol_array = np.array(np.absolute(array))  # array([12, 25, 31])
sqrt_array = np.array(np.sqrt(absol_array))  # array([3.46410162, 5.   , 5.56776436])
round_array = np.array(np.round(sqrt_array))  # array([3., 5., 6.])
round_down_array = np.array(np.floor(sqrt_array))  # array([3., 5., 5.])
round_up_array = np.array(np.ceil(sqrt_array))  # array([4., 5., 6.])

# Exercise

radius = np.array([1, 2, 3])
circle_area = np.pi * (radius**2)

for i in range(len(radius)):
    print(
        f"the area of a circle with where radius is {radius[i]} is equall to {circle_area[i]} "
    )

# Elemet-wise arithmetic

array = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

 print(array + array2) # [5 7 9]
 print(array - array2) # [-3 -3 -3]
 print(array * array2) # [4 10 18]
 print(array / array2) # [0.25 0.4 0.5]
 print(array ** array2) # [1 32 729]

# Comparison operator + Exercise

scores = np.array([12,3,20,15,13.5,9.75,10,2.5])
pass_score = scores >= 10
for i in range(len(pass_score)):
   if pass_score[i] == True:
      print(f'You passed with {scores[i]}')
   else:
      print(f'You didn`t pass with {scores[i]}')

'''
You passed with 12.0
You didn`t pass with 3.0
You passed with 20.0
You passed with 15.0
You passed with 13.5
You didn`t pass with 9.75
You passed with 10.0
You didn`t pass with 2.5
'''

# Broadcasting + Exercise
array1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
array2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

print(array1.shape , array2.shape) # (1, 10) (10, 1)
muti_table = array1 * array2
'''array([[  1,   2,   3,   4,   5,   6,   7,   8,   9,  10],
       [  2,   4,   6,   8,  10,  12,  14,  16,  18,  20],
       [  3,   6,   9,  12,  15,  18,  21,  24,  27,  30],
       [  4,   8,  12,  16,  20,  24,  28,  32,  36,  40],
       [  5,  10,  15,  20,  25,  30,  35,  40,  45,  50],
       [  6,  12,  18,  24,  30,  36,  42,  48,  54,  60],
       [  7,  14,  21,  28,  35,  42,  49,  56,  63,  70],
       [  8,  16,  24,  32,  40,  48,  56,  64,  72,  80],
       [  9,  18,  27,  36,  45,  54,  63,  72,  81,  90],
       [ 10,  20,  30,  40,  50,  60,  70,  80,  90, 100]])'''

# Aggregate functions
 
array = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(np.sum(array)) #55
print(np.min(array)) #1
print(np.max(array)) #10
print(np.mean(array)) #5.5
print(np.argmin(array)) # 0 
print(np.argmax(array)) # 9 

print(np.sum(array, axis = 0)) # [ 7  9 11 13 15]
print(np.sum(array, axis = 1)) # [15 40]

# Filtering
ages = np.array([[21,19,15,23,20,18,16,43],
                 [39,28,22,17,19,20,24,25]])
ages.shape
teenages = ages[ages < 18] #[15, 16, 17]
adults = ages[(18 <= ages) & (ages <= 25)] # [21, 19, 23, 20, 18, 22, 19, 20, 24, 25]
not_in_collage = ages[(18 > ages) | (ages > 25)] # [15, 16, 43, 39, 28, 17]
evens = ages[ages % 2 == 0] # [20, 18, 16, 28, 22, 20, 24]
odds = ages[ages % 2 == 1] # [21, 19, 15, 23, 43, 39, 17, 19, 25]

new_adults = np.where( (18 <= ages) & (ages <= 25)  , ages , -1) 
# [[21, 19, -1, 23, 20, 18, -1, -1],[-1, -1, 22, -1, 19, 20, 24, 25]]

# random number generator + exercise
rng = np.random.default_rng(seed=1)

print(rng.integers(low=1,high=7,size=(3,2))) # random dice number 3 turns 2 players 
''' my example :
[[3 4] player 1 = 3, player 2 = 4
 [5 6] player 1 = 5, player 2 = 6
 [1 1]] player 1 = 1, player 2 = 1
 '''
np.random.seed(seed=1)
rng_range = np.random.uniform(low=-1,high=1) # -0.165955990594852

array = np.array([1,2,3,4,5])
rng.shuffle(array) # [4, 1, 2, 5, 3]
fruits = np.array(['apple','banana','orange','kiwi','pineapple'])
rand_fruit = rng.choice(fruits , size=(2,3)) 
''' 
[['apple', 'apple', 'pineapple'], 
['kiwi', 'pineapple', 'orange']]  => random choises
'''