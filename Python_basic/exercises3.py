# 1- color_list_1'den color_list_2'DE olmayan tüm renkleri yazdıran bir Python programı yazın. 

color_list_1 = set(["White","Black","Red"])
color_list_2 = set(["Red","Green"]) 

# difference of color_list_1 from color_list_2
print(color_list_1.difference(color_list_2))
# difference of color_list_2 from color_list_1 
print(color_list_2.difference(color_list_1))

# 2- Write a Python program that will accept the base and height of a triangle and compute its area. 

b = 5
h = 10

def volume():
    v = b*h/2
    return v

print(volume())

# 3- Write a Python program that computes the gratest common divisor (GCD) of two positive integers. 

def gcd(x,y):
    gcd = 1
    if x % y == 0:
        return y
    for k in range(int(y/2), 0 , -1):
        if x % k == 0 and y % k == 0:
            gcd = k 
            break
    return gcd

print(gcd(10,15))
print(gcd(48,96))
        
# 4- Write a Python program to find the least common multiple (LCM) of two positive integers. 

def lcm(x, y):
    if x > y:
        z = x
    else:
        z = y
    while(True):
        if((z % x == 0) and (z % y == 0)):
            lcm = z
            break
        z += 1
    return lcm
print(lcm(23,34))
print(lcm(11,56))

# 5- Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero. 

n1 = int(input("Enter a first number: "))
n2 = int(input("Enter a second number: "))
n3 = int(input("Enter a third number: "))

def total():
    if (n1 == n2) or (n2 == n3) or (n1 == n3):
        sum = 0
        return sum
    else:
        x = n1+ n2 + n3
        return x

print(total())

# 6- Write a Python program to sum two given integers. However, if the sum is between 15 and 20 will return 20. 

num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))

def sum(num1, num2):
    sum = num1 + num2
    if sum in range(15,20):
        return 20
    return sum

print(sum(num1,num2))


# 7- Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5. 

def number(num1,num2):
    if (num1 == num2) or abs(num1 - num2) == 5 or (num1 + num2) == 5:
        return True
    else:
        return False

print(number(10,10))
print(number(34,29))
print(number(5,20))

# 8- Write a Python program to add two objects if both objects are integers. 

def sum(num1, num2):
    if not (isinstance(num1, int) and isinstance(num2, int)):
        return "Both values most be integer"
    else:
        return num1 + num2

print(sum(10,20))
print(sum(2.5,10))

# 9- Write a Python program to solve (x + y) * (x * y)

def math(x,y):
    result = (x + y) * (x + y)
    return result

print(math(4,3))

# 10- Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years. 

amount = 10000
interest = 3.5    
years = 7
def future_value():
    future_value = amount*((1+(0.01*interest)) ** years)
    return future_value

print(future_value())

# 11- Write a Python program to calculate the distance between the points (x1,y1) and (x2,y2)

import math

def distance(p1,p2):
    distance = math.sqrt( ((p1[0] - p2[0]) **2) + ((p1[1] - p2[1]) ** 2))
    return distance

print(distance([4,0],[6,6]))  

