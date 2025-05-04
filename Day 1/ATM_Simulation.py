# Initial bank account details
balance = 5000  # Starting balance

print("Welcome to the ATM!\n")

# Simulate the ATM interaction using a while loop
while True:
    print("\nPlease select an option:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        print(f"Your current balance is: ₹{balance}")
    elif choice == '2':
        deposit = float(input("Enter the amount to deposit: ₹"))
        balance += deposit
        print(f"₹{deposit} deposited successfully. New balance: ₹{balance}")
    elif choice == '3':
        withdraw = float(input("Enter the amount to withdraw: ₹"))
        if withdraw > balance:
            print("Insufficient balance! Please try again with a smaller amount.")
        else:
            balance -= withdraw
            print(f"₹{withdraw} withdrawn successfully. New balance: ₹{balance}")
    elif choice == '4':
        print("Thank you for using the ATM. Have a nice day!")
        break  # Exit the loop and end the program
    else:
        print("Invalid choice! Please select a valid option.")
