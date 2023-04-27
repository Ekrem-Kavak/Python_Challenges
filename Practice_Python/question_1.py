# QUESTION - 1

# Create a program that asks the user to enter their name and their age. Print out a message adressed to them that tells them the year that they will turn 100 years old. 

name = input("Enter a name: ")
age = int(input("Enter an age: "))
years = 2023 + (100 - age)
print(f"Hi {name}! In {years} you will turn 100 years old")

