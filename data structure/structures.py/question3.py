
# Write a Python function that accepts a list and returns a new list with only
# the even numbers from the original list.

main_lists = []
even_lists = []
number = int(input("Enter the number of elements you want to add in the list: "))

for value in range(number):
    temp = int(input("Enter the element: "))
    main_lists.append(temp)

for value in range(number):
    if(main_lists[value] % 2 == 0):
        even_lists.append(main_lists[value])

print(even_lists)