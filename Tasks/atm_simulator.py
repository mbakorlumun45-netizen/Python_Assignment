
balance = 1000

while balance != 0:
	print("atm main options")
	atm_menu = """
	1 deposit
	2 withdrawal
	3 check balance
	"""
	print(atm_menu)
	choice = int(input("choose an option"))
	if choice == 1:
		deposit = int(input("Enter Amount to deposit: "))
		balance += deposit
            print("Enter a positive number")
            break
		print("deposit successful")
		print("The balance is:", balance)
		break
        
    print("deposit successful")
    print("The balance is: ", balance)	
    break
	
	elif choice ==2:
		withdrawal = int(input("Enter withdrawal amount: "))
		
		if withdrawal > balance:
			print("Insufficient funds")
		else:
			balance -= balance withdrawal
			print("withdrawal successful")
			print("The remaining balance is:", balance)
			
	elif choice == 3:
		print("Your balance is:", balance)
		
	else:
		print("Invalid option")
	break

