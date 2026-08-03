number = int(input("Enter a number"))

for number in range(1, 11):
	for count in range(1, 11):
	
		product = number * count
	
		print(f"{number:<3} x {count} = {product:<4}", end= "")
	print()
