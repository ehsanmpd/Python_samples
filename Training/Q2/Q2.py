number = input("Insert a number to compute its factorial: ")
type(number)
number = int(number)
factorial = 1
for i in range(1,number+1):
    factorial *= i
print(str(factorial))