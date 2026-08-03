#number = 3, 4, 5, 6, 7, 8, 9
 
list = (3, 4, 5, 6, 7, 8, 9)
even_num = 0
odd_num = 0
for number in list:

	if number % 2 == 0:
		even_num = even_num + 1
		
	else :
		odd_num = odd_num +1
		
print("Number of even numbers is: ", even_num)
print("Number of odd numbers is: ", odd_num)
