# Write a program that finds all numbers between 100 and 999 where the sum
# of the cubes of the digits equals the number itself (Armstrong numbers).
lists = []

for value in range(100, 1000):
    hundredth_place = int(value / 100)
    tenth_place = int((value / 10) % 10)
    ones_place = int((value % 10))

    sum = hundredth_place**3 + tenth_place**3 + ones_place**3

    if(sum == value):
        lists.append(value)
    
print(f"\nThe lists of amstrong number from 100 to 999 is {lists}")


