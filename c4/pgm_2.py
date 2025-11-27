class BankAccount:
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully!")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully!")


    def show_details(self):
        print("\n---- Account Details ----")
        print("Account Number:", self.acc_no)
        print("Name:", self.name)
        print("Account Type:", self.acc_type)
        print("Balance: ₹", self.balance)



acc_no = input("Enter Account Number: ")
name = input("Enter Account Holder Name: ")
acc_type = input("Enter Account Type (Savings/Current): ")
balance =0
# Creating account object
account = BankAccount(acc_no, name, acc_type, balance)

# Menu for user
while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Show Account Details")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == 3:
        account.show_details()

    elif choice == 4:
        print("Thank you for banking with us!")
        break

    else:
        print("Invalid choice! Try again.")
