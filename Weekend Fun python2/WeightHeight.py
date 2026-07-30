#collect input for weight and height
#multiply height by itself
#divide the product of sum with weight
#assign each number given to the product of the input 
#condition it to print base on the product of the input 
weight = int(input("Enter weight"))
height = int(input("Enter height"))

result = weight/(height * height)

if(result < 18.5):
	print("underweight")
	
elif(result >= 18.5 and result <= 24.9):
	print("Normal")
	
elif(result >= 25 and result <= 29.9):
	print("Overweight")
	
elif(result >= 30):
	print("Obese")
