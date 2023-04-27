# QUESTION - 2

# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
# a) If the number is a multiple 4, print out a different message. 
# b) Ask the user two numbers: one number to check and one number to divides evenly into, tell that to the user. If not, print a different apropriate message. 

number = int(input("Enter a number: "))

if (number % 2 == 0):
    print("The number is 'odd'")    
elif(number % 2 == 1):
    print("The number is 'even'")


# EXTRA

check_number = int(input("Enter a check number:"))

if (number % 2 == 0) and (number % 4 != 0):
    print("The number is 'odd'")    
elif(number % 2 == 1):
    print("The number is 'even'")
elif(number % 4 == 0): 
    print("This number is divisible by four")

if number % check_number == 0:
    print(f"The number {number} is divisible by the check_number")
else:
    print(f"{number} number is not divisible by check_number")





