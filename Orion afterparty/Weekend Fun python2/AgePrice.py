#collect input from user
#assign each age range to a purchase status
#condition each to do what
#print each one when the condition is true
age = int(input("Enter age"))

if(age < 5):
	print("Free")
	
if(age >= 12 and age < 13):
	print("5, dollars")
	
if(age >= 13 and age < 64):
	print("12, dollars")
	
elif(age >= 65):
	print("8, dollars")
