# Write a Python program to remove all duplicates from a list and print the
# unique elements.

test_list = []
number = int(input("Enter the number of elements you want to add in the list: "))

for value in range(number):
    temp = input("Enter the element in the list: ")
    test_list.append(temp)

unique_set = set(test_list)
print(f"{unique_set}")