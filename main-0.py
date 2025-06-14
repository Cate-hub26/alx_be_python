import sys
from programming_paradigm.bank_account import BankAccount  # Adjusted import path

def main():
    account = BankAccount(200)  # Set up an account with an initial balance

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    # Execute the correct method based on the command
    if command == "deposit" and amount is not None:
        account.deposit(amount)  # Only prints deposit message
    elif command == "withdraw" and amount is not None:
        account.withdraw(amount)  # Only prints withdraw message
    elif command == "display":
        account.display_balance()  # Only prints balance
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()