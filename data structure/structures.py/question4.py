
# Write a program to count the number of each character in a given string
# using a dictionary.

dict = {}
test_string = input("Enter the value of the test string : ")

for value in (test_string):
    if value not in dict.keys():
        dict[value] = test_string.count(value)

print(dict)





























