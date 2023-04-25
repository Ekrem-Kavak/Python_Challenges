# 1- Write a Python program that accepts an integer (n) and computes value of n + nn + nnn

number = int(input("Enter a integer: "))
n1 = int("%s" %number)
n2 = int( "%s%s" % (number,number))
n3 = int( "%s%s%s" % (number,number,number))
print(n1 + n2 + n3)

# 2- Write a Python program that prints the calendar for a given month and year
"""
import calendar 
y = int(input("Input the year: "))
m = int(input("Input the month: "))
print(calendar.month(y,m))
"""
# 3- Write a Python program to calculate the number of days between two dates. 
"""
from datetime import datetime

date_str1 = input("Enter the first date (dd/mm/yyyy): ")
date1 = datetime.strptime(date_str1, "%d/%m/%Y")
date_str2 = input("Enter the second date (dd/mm/yyyy): ")
date2 = datetime.strptime(date_str2, "%d/%m/%Y")

delta = date2 - date1
days = delta.days

print("Number of days between the dates: ", days)
"""

# 4- Write a Python program to get the volume of a sphere with radius six. 

r = 6
pi = 3.14

def volume():
    V = 4/3 * pi * r**3
    return V

print(volume())     


# 5- Write a Python program to calculate teh difference between given number and 17. If the number is greater than 17, return twice the absolute difference. 

number = int(input("Enter a number: "))

def difference(number):
    if (number <= 17):
        return number - 17
    elif(number > 17):
        return 2*(number - 17)

print(difference(number))
    
# 6- Write a Python program to test whether a number is within 100 of 1000 or 2000. 

def thousand(n):
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100)) 

print(thousand(5000))
print(thousand(1900))

# 7- Write a Python program to get a newly-generated string a from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins is "Is".

text = input("Write a text: ")

def texting(text):
    if len(text) >= 2 and text[:2] == "Is":
        return text
    else:
        return "Is" + text

print(texting(text))

# 8- Write a Python program that returns a string that is n (non-negative integer) copies of a given. 

def larger_string(text, n):
    result = ""
    for i in range(n):
        result = result + text
    return result 
print(larger_string("kvk", 3))        

    
# 9- Write a Python program that determines whetwer a given number (accepted from the user) is even or odd, adn prints an appropriate message to the user. 

number = int(input("Enter a number: "))

def even_odd(number):
    if (number % 2 == 0):
        return f"Number is even"
    else:
        return f"Number is odd"

print(even_odd(number)) 

# 10- Write a Python program to count the number 4 in a given list. 

def list_count(nums):
    count = 0
    for num in nums:
        if num == 4:
            count += 1
    
    return count

print(list_count([2,3,4,4,6,4,99,44,4,4])) # 5


# 11- Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the lenght in less than 2. 

def texting(text,n):
    flen = 2
    if (flen > len(text)):
        flen = len(text)
    new_text = text[:flen]
    result = ""
    for i in range(n):
        result = result + new_text
    return result

print(texting("Python",7))
print(texting("J", 2))

# 12- Write a Python to test whether a passed letter is a vowel or not. 

def vowel(letter):
    all_vowels = "aeıioöuü"
    return letter in all_vowels

print(vowel("e"))

# 13- Write a Python program that checks whether a specified value is contained a group of values. 

def group_member(numbers,n):
    for value in numbers:
        if n == value:
            return True
    return False

print(group_member([1,2,3,4],7)) # false
print(group_member([1,2,3,4],2)) # True

