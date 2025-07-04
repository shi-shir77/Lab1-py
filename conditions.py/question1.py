# Write a program to check whether a given number is prime or not.
number = int(input("Enter a number : "))

if (number > 1):
    is_prime = True
    for value in range(2, int(number ** 0.5) + 1):
        if (number % value == 0):
            is_prime = False
            break

    if (is_prime):
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
else:
    print("Enter a valid number greater than 1")
