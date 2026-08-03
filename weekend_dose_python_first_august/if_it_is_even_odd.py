number = int(input("Enter number: "))

steps = 0

while number != 1:
	if number % 2 == 0:
		number = number // 2
		
	else:
		number = (number * 3) + 1
	steps += 1
	
print(steps)
		
 




















#for count in range(number, 1):
	#if number % 2 == 0:
		#number = number // 2
	#else : 
		#sum_odd = (number * 3) + 1
	#steps += 1
		
	
#print(steps)

