# Write a program to print the multiplication table of a given number using a
# for loop.

number = int(input("Enter a number : "))

for value in range(1, 11):
    print(f"{number} * {value} = {number * value}")
