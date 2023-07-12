# LISTS QUESTIONS

# 1- Write a Python program to sum all the items in a list. 

numbers = [1,3,4,10,-2]

def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list(numbers))

# 2- Write a Python program to multiply all the items in a list. 

numbers = [2,5,10,-20]

def mult_list(items):
    mult_list = 1
    for item in items:
        mult_list *= item
    return mult_list
print(mult_list(numbers))
    
# 3- Write a Python program to get the smallest number from a list. 

def large_numb(number):
    max = number[0]
    for numb in number:
        if numb > max:
            max = numb
    return max
print(large_numb([15,32,10,75,65]))

# 4- Write a Python program to get the smallest number from a list 


numbers = [-5,-10,-40,-100]

def small_numb(number):
    min = number[0]
    for numb in number:
        if numb < min:
            min = numb
    return min
print(small_numb(numbers))


# 5- Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same. 

def match_words(words):
    ctr = 0

    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
    return ctr

print(match_words(["4554","abba","sedse","3553"]))




