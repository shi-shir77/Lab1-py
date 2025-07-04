# Write a program to find the largest and smallest number in a list entered by
# the user.

lists = []
number_of_items = int(
    input("Enter the number of items you want to enter inside list: "))

for value in range(number_of_items):
    num = int(input("Enter a integer: \n"))
    lists.append(num)

print(f"The smallest number in a list is {min(lists)}")
print(f"The largest number in a list is {max(lists)}")
