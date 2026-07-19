#collect input from user for x and y seperate
#print Q1 if x > 0 and y>0
#print Q2 if x<0 and y>0
#printQ3 if x<0 and y<0
#printQ4 if x>0 and y<0
#print origin if both are 0
#print x-axis if y==0 and x !=0
#y-axis if x == 0 and y != 0

x = int(input("Enter an integer"))

y = int(input("Enter an integer"))

if(x > 0 and y > 0):
	print(Q1)
	
elif(x < 0 and y > 0):
	print("Q2")
	
elif(x < 0 and y < 0):
	print("Q3")
	
elif(x > 0 and y < 0):
	print("Q4")
	
elif(x == 0 and y == 0):
	print("origin")
	
elif(y == 0 and x != 0):
	print("x-axis")
	

