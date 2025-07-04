
# Create a tuple of 10 integers. Write a program to display the maximum and
# minimum numbers from the tuple.

lists = []

for value in range(1, 11):
    temp = int(input(f"Enter the element {value}: "))
    lists.append(temp)

test_tuple = tuple(lists) #converting the list into tuple using tuple() function

print(f"The maximum number from the tuple is {max(test_tuple)}")
print(f"The minimum number from the tuple is {min(test_tuple)}")

