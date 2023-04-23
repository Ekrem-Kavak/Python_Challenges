# 1- Write a Python program that calculates the area of a circle based on the radius entered by the user. 

r = int(input("Enter a radius "))
def radius(r):
    pi = 3.14
    area = pi*r**2
    return area

print(radius(r))    

# 2- Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them

def reverse_name():
    name = input("Name: ")
    surName = input("Surname: ")
    print(surName + " " + name)

reverse_name()

# 3- Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.

number = input("Enter the numbers")
list = number.split(",")
tuple = tuple(list)
print(f"Liste: ",list)
print(f"Demet: ",tuple)

# 4- Write a Python program that accepts a filename from the user and prints the extension of the file.

file = input("Enter a filename: ")
extensions = file.split(".")
print(extensions[-1])

# 5- Write a Python program to display the first and last colors from the following list. 
# color_list = ["Red","Green","White","Black"]

color_list = ["Red","Green","White","Black"]

first = color_list[0]
last = color_list[-1]
print(f"First element {first}, last element {last}")
