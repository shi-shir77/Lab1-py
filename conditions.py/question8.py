# Write a program that reads a number and prints whether it is a palindrome or
# not.

number = (input("Enter the number : "))

if(number == number[::-1]):
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")


