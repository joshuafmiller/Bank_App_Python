

class Bank:

    def __init__(self, initial_amount=0.00):
        self.balance = initial_amount

    def log_transaction(self, transaction_string):
        with open("transactions.txt", "a") as file:
            file.write(f"{transaction_string}\n")

    def withdrawal(self, amount):

        try:
            amount = float(amount)
        except ValueError:
            amount = 0    

        if amount:
            self.balance = self.balance - amount
            self.log_transaction(f"Withdrew ${amount}      Balance: ${self.balance}")
    
    def deposit(self, amount):

        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance + amount
            self.log_transaction(f"Deposited ${amount}      Balance: ${self.balance}")
            

account = Bank(50.50)

while True:

    action = input("Do you want to withdrawal or deposit? ")
    if action == "withdrawal":
        amount = input("How much do you want to take out? ")
        account.withdrawal(amount)
    if action == "deposit":
        amount = input("How much do you want to deposit? ")
        account.deposit(amount)
    else:
        print("Enter a valid option")
    print(f"Your balance is {account.balance}")

