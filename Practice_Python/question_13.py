# QUESTION - 14

# Write a program that takes a list and returns a new list that contains all the elements of the first list minutes all the duplicates. 

def list_v1(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y

def list_v2(x):
    return list(set(x))

a = [1,2,3,6,17,17,30,35,35,35,100]
print(a)
print(list_v1(a))
print(list_v2(a))