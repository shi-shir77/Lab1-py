# Create a set of prime numbers less than 50. Write a program to check
# whether a given number exists in the set or not.

prime_set = set()
for num in range(2, 51):
    is_prime = True

    for value in range(2, int(num ** 0.5) + 1):
        if(num % value == 0):
            is_prime = False
            break

    if (is_prime):
         prime_set.add(num)
            
test_element = int(input("Enter the number you want to check if it exists in the set or not: \n"))

if test_element in (prime_set):
    print(f"{test_element} exists in the set of prime numbers less than 50. \n")
else:
    print(f"{test_element} doesn't exists in the set of prime numbers less than 50. \n")

