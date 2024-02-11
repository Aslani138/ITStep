class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposit successful. New balance: {self.balance}"
        else:
            return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        elif amount <= 0:
            return "Invalid withdrawal amount"
        else:
            self.balance -= amount
            return f"Withdrawal successful. New balance: {self.balance}"

# Creating accounts
account1 = BankAccount("123456", "Daviti", 1000)
account2 = BankAccount("789012", "Mariami", 500)

# Perform transactions
print(account1.deposit(500))  # Deposit into account1
print(account1.withdraw(200))  # Withdraw from account1
print(account2.deposit(300))  # Deposit into account2
print(account2.withdraw(900))  # Withdraw from account2 (should show insufficient balance)
