# Write a program that accepts 10 integers from the user and counts how many
# are positive, negative, and zero.

lists = []
positive_lists = []
negative_lists = []
zero_lists = []

number_of_items = int(
    input("Enter the number of items you want inside the list : "))
for value in range(number_of_items):
    temp = int(input("Enter the value of an integer : "))
    lists.append(temp)

for value in range(number_of_items):
    if (lists[value] > 0):
        positive_lists.append(lists[value])
    elif (lists[value] < 0):
        negative_lists.append(lists[value])
    else:
        zero_lists.append(lists[value])

print(f"\nThe total number of the positive items in the list is {len(positive_lists)} i.e {positive_lists}")
print(f"\nThe total number of the negative items in the list is {len(negative_lists)} i.e {negative_lists}")
print(f"\nThe total number of the zero items in the list is {len(zero_lists)} i.e {zero_lists}")
