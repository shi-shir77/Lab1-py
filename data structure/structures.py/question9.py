# Write a Python program to remove elements from a list that are also present
# in another list.

list1 = []
num1 = int(input("Enter the number of elements you want to add in the list: "))

for value in range(num1):
    temp = int(input("Enter the element : "))
    list1.append(temp)

list2 = []
num2 = int(input("Enter the number of elements you want to add in the list: "))

for value in range(num2):
    temp = int(input("Enter the element : "))
    list2.append(temp)

print(f"Original List: {list1}")
print(f"Original List: {list2}")
    
for value in list1[:]: #iterating over the copy of list1 coz when we remove the item from the list1 the list get shorter so we need to iterate over the copy of the list1
    if value in list2:
        list1.remove(value)

print(f"The new list is {list1}")
