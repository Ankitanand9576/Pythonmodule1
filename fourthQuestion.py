""" Write a Python script that uses a for loop to sum up all numbers in a list that are greater than 10. Use if-else within the loop to decide
which numbers """
listDemo=[21,34,5,78,45,2,9,4,]
sumOfDigit=0
for i in listDemo:
    if i > 10:
        print(i)
        sumOfDigit=sumOfDigit+i

print(f"sum of digits greater than 10 in list {sumOfDigit}")