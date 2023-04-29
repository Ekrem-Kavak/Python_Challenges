# QUESTION - 3:

# Take a list, say for example this one:
# numbers = [1,1,2,3,5,8,13,21,34,55,89]
# and write a program that prints out all the elements of the list that are less than 5. 

# Extras:

# 1- Instead of printing the elements one by one, make a new list that has all the elements. 
# 2- Write this is one line of Python. 
# 3- Ask the user for a number and return a list that contains only elements from the original list a that are smaller than number given by the user. 

numbers = [1,1,2,3,5,8,11,21,34,55,89]

for number in numbers:
    if (number < 5):
        print(number) 

# Extra - 1

less_numbers = []

for number in numbers:
    if (number < 5):
        less_numbers.append(number)
print(less_numbers)        

# Extra - 2

print([number for number in numbers if number < 5])

# Extra - 3


give_numb = int(input("Enter a number:"))    
new_list = []

for number in numbers:
    if (number < give_numb):
        new_list.append(number)

print(new_list)

