# Let's say I give you list a saved in a variable
# numbers = [1,4,9,16,25,36,49,64,81,100]
# Write one line of Python that takes this list a and makes a new lis tthat has only the even elements of this list in it.

numbers = [1,4,9,16,25,36,49,64,81,100]

even_list = []

for number in numbers:
    if (number % 2 == 0):
        even_list.append(number)

print(even_list)

# single line

even_list = [number for number in numbers if number % 2 == 0]
print(even_list)