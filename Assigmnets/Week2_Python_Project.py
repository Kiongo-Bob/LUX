# Python. Given an array of integers, find the sum of its elements.
import numpy as np

# Generate a random uni-dimensional array of 10 integers like teenagers' ages
rand_int_arr = np.random.randint(13, 19, 10)
print(rand_int_arr)

#Getting the sum of the generaed ages using a loop
sum_loop = 0

for i in rand_int_arr:
    sum_loop += i
print(sum_loop)    
#Getting the sum using sum function
sum_arr = np.sum(rand_int_arr)
print(sum_arr)

<<<<<<< HEAD
print(sum_loop == sum_arr)

=======
print(sum_loop == sum_arr)
>>>>>>> e8b22a11315acb5f1754f3c51be05919391d6782
