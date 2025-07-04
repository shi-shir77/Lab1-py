# Write a program that reads a number and prints the factorial of that number
# using a while loop.

number = int(input("Enter a number : "))
loop_count = 1
factorial = 1

if (number < 0):
    print("Invalid Number. Please enter a number greater than or equal to zero")
elif (number == 0):
    print("The factorial of 0 is 1")
else:
    loop_count = 1
    while (loop_count <= number):
        factorial *= loop_count
        loop_count += 1
    print(f"The factorial of the {number} is {factorial}")
