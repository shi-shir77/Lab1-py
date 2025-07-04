# Given a list of names, write a program to count how many times each name
# appears using a dictionary.

name_lists = []
number = int(input("Enter the number of names you want to add in the list: "))

for value in range(number):
    temp = input("Enter the name: ")
    name_lists.append(temp)

name_count = {}
for name in name_lists:
    if name in name_count.keys():
        name_count[name] += 1
    else:
        name_count[name] = 1

print(name_count)
        

