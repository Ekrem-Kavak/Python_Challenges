# QUESTION - 6

# Ask the user for a string and print out whether this string is a palindrome or not.

row = input("Enter a word: ")

row = str(row)
print(row)
reverse_row = row[::-1]
print(reverse_row)

if row == reverse_row:
    print("This word is a palindrome")
else:
    print("This word is a not palindrome")

