def commission_deduction(func):
    def wrapper(balance, amount):
        commission = 1  # Commission amount in GEL
        total_amount = amount + commission

        if balance < total_amount:
            return "Error: Insufficient balance to complete the transaction."

        return func(balance, amount)
    
    return wrapper

@commission_deduction
def process_payment(balance, amount):
    new_balance = balance - amount - 1  # Deducting the amount and commission
    return f"Payment successful. New balance is {new_balance} GEL."

# Example usage
print(process_payment(100, 50))  # Sufficient balance
print(process_payment(20, 25))   # Insufficient balance
