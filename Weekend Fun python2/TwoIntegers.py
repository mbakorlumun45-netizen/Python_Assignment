#collect input from the user
#divide x with y
#print the result of xy if the rsult is not equal to zero
#print cannot divide by zero if the result is equal to zero
x = int(input("Enter first integer"))
y = int(input("Enter second integer"))

result = (x / y)

if(result != 0):
	print(result)
	
if(result == 0):
	print("Cannot divide by zero")
