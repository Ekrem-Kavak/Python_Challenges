# QUESTION - 5

# Take two list, say for example these two:
# a = [1,1,2,3,5,8,13,21,34,55,89]
# b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# and write a program that returns a list contains only the elements that are common between the lists. Make sure your program works on two list of different sizes. 
# Extra:
# 1- Randomly generate two lists to test this. 

a = [1,1,2,3,5,8,13,21,34,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13]

a = set(a)
b = set(b)

intersection_set = a.intersection(b) # A U B
print(intersection_set)
print("---")
# Extra - 1: 
import random 

a = [random.randint(1,100) for i in range(10)]
b = [random.randint(1,100) for i in range(10)]

a = set(a)
b = set(b)
print(a)
print(b)
intersection_random_set = a.intersection(b)
print(intersection_random_set)
