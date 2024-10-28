class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}")

    def display_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Balance: {self.balance}")


 # Creating instances (objects) of BankAccount
account1 = BankAccount(101, "Alice", 5000)
account2 = BankAccount(102, "Bob", 3000)

# Using methods
account1.deposit(2000)
account1.withdraw(1000)
account1.display_info()

account2.deposit(1500)
account2.withdraw(3500)
account2.display_info()

# OUTPUT:-
# Deposited 2000. New balance is 7000
# Withdrew 1000. New balance is 6000
# Account Number: 101
# Holder Name: Alice
# Balance: 6000
# Deposited 1500. New balance is 4500
# Withdrew 3500. New balance is 1000
# Account Number: 102
# Holder Name: Bob
# Balance: 1000