# Given two lists, write a program to find their intersection using sets.

lists1 = []
lists2 = []

num1 = int(input("Enter the number of elements you want to add in the list 1 : \n"))
for value in range(num1):
    temp = int(input("Enter the element : "))
    lists1.append(temp)

num2 = int(input("\nEnter the number of elements you want to add in the list 2 : \n"))
for value in range(num2):
    temp = int(input("Enter the element : "))
    lists2.append(temp)

set1 = set(lists1)
set2 = set(lists2)

print(f"\nThe intersection of the sets are {set1.intersection(set2)}")
