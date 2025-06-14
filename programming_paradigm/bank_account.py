class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance
        
    def deposit(self, amount1):
        if amount1 > 0:
            self.account_balance += amount1
            print(f"Deposited: ${amount1}")
        else:
            print("Invalid deposit amount.")
    
    def withdraw(self, amount2):
        if amount2 > 0 and amount2 <= self.account_balance:
            self.account_balance -= amount2
            print(f"Withdrew: ${amount2}")
            return True
        else:
            print("Insufficient funds.")
            return False
        
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")
        return f"Current Balance: ${self.account_balance}."
        
bankaccount = BankAccount(200)
bankaccount.deposit(50.0)
bankaccount.withdraw(20.0)
bankaccount.display_balance()