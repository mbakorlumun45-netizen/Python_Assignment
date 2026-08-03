

def checkings(item, price, code):

save_ten = price - 0.10
half_off = price - 0.50
		
	if code >= 10:
		return save_ten
		
	if code >= 50:
		return half_off
	 

item = str(input("Enter item name: "))
price = int(input("Enter original price: "))
code = int(input("Enter a promotional code: "))

result = checkings(item, price, code):  

print = (result)
