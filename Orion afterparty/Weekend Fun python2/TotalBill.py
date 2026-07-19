# collect input for total bill
#collect input for member
#condition the statement to discount 10% if the user is a member and the bill is greater than 1000
#condition the other statement to print 5% if the bill is 1000 but the user is not a member
#print no discount if the user does not meet both conditions
total_bill = int(input("total bill"))

member = input("Are you a member (yes or no):")

if(total_bill >= 1000 and member == yes):
	print("discount 10% off")
	
elif(total_bill >= 1000 and member == no):
	print("discount 5% off") 
	
else: print("No discount")	
