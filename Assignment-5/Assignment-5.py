# Assignment 5
# Aim: Implement a BankAccount class

class BankAccount:
    def __init__(self, acc_no, holder_name, balance=0):
        self.acc_no = acc_no
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid withdrawal amount!")
        else:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}")

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")


# Creating object
account1 = BankAccount(12345, "Yatharth", 10000)

account1.check_balance()
account1.deposit(2000)
account1.withdraw(5000)
account1.check_balance()

