balance = 1000

while True:
    print("\nATM Main Options")
    atm_menu = """
1. Deposit
2. Withdrawal
3. Check Balance
4. Exit
"""
    print(atm_menu)

    choice = int(input("Choose an option: "))

    if choice == 1:
        deposit = int(input("Enter amount to deposit: "))

        if deposit > 0:
            balance += deposit
            print("Deposit successful.")
            print("Your balance is:", balance)
        else:
            print("Enter a positive amount.")

    elif choice == 2:
        withdrawal = int(input("Enter withdrawal amount: "))

        if withdrawal <= 0:
            print("Enter a positive amount.")
        elif withdrawal > balance:
            print("Insufficient funds.")
        else:
            balance -= withdrawal
            print("Withdrawal successful.")
            print("Remaining balance is:", balance)

    elif choice == 3:
        print("Your balance is:", balance)

    elif choice == 4:
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid option.")
