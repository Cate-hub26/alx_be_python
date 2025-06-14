class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance
        
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Invalid deposit amount.")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew: ${amount:.2f}")
            return True
        else:
            print("Insufficient funds.")
            return False
        
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")
        return f"Current Balance: ${self.account_balance}."
       
bankaccount = BankAccount(10000.00)
bankaccount.deposit(2000.00)
bankaccount.withdraw(230.00)
bankaccount.display_balance()