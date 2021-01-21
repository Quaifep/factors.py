# Author: Paul Quaife
# Date: 1/19/2020
# Description: Gives whole factors of given number.

var = int(input("Please enter a positive integer: "))
print("The factors of", var, "are:")
for num in range(1, var+1,):
    if var % num == 0:
        print(num)
