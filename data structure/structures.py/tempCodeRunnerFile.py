
items = {}
number = int(input("Enter the number of items you want to add in the store : "))

for value in range(number):
    name = input("Enter the name of the food: ")
    cost = input("Enter the price : ")
    items[name] = cost


user_request = input("Enter the food name you want to search : ")
print(items[user_request])