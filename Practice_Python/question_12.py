# QUESTION - 13

"""
Write a program that asks the user how many Fibonacci numbers to generate and then generates them. Takes this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate. 

"""
def fib_num():
    fibonacci = int(input("How many elements do you want for a fibonacci sequence? "))
    i = 1
    if (fibonacci == 0):
        fib = []
    elif (fibonacci == 1):
        fib = [1]
    elif (fibonacci == 2):
        fib = [1,1]
    elif (fibonacci > 2):
        fib = [1,1]
        while i < (fibonacci - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1

    return fib

print(fib_num())
