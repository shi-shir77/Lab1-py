# Write a program to generate the Fibonacci sequence up to n terms.

number = int(input("Enter the number of terms of fibonnaci sequence you want to obtain: "))
first_term = 0
second_term = 1

print("Fibonnaci sequence : ")
for count in range(number + 1):
    print(f"{first_term}")
    next_term = first_term + second_term
    first_term = second_term
    second_term = next_term