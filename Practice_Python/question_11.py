# QUESTION - 11

# Write a program that takes a list of numbers and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

list_numb = input("Enter multiple numbers (comma separated numbers)")
list_numb = list_numb.split(",")

def new_list(list_numb):
    return [list_numb[0], list_numb[len(list_numb)-1]]

print(new_list(list_numb))
    

