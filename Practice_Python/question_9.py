# QUESTION - 9

# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, tell them whether they guessed too low, too high or exactly right. 

# EXTRA 
# 1- Keep the game going until the user types "exit" 
# 2- Keep track of how many guesses the user has taken, and when the game ends, print this out. 

import random 

rand_num = random.randint(1,9)
number = 0
h = 0
while number != rand_num and number != "exit":
    number = int(input("Write a number between 1 and 9:  "))

    if number == "exit":
        break

    number = int(number)
    h += 1

    if number < rand_num:
        print("Please enter a higher number")
    elif number > rand_num:
        print("Please enter a lower number")
    else:
        print("Congratulations, correct number!")
        print("You took only", h , "tries")


    

