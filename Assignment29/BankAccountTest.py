import unittest
from bank_account import BankAccount

# Test cases for BankAccount class
class TestBankAccount(unittest.TestCase):
    def test_deposit_positive_amount(self):
        account = BankAccount("12345", "John Doe", 100)
        self.assertEqual(account.deposit(50), "Deposited $50. New balance: $150")

    def test_deposit_zero_amount(self):
        account = BankAccount("12345", "John Doe", 100)
        self.assertEqual(account.deposit(0), "Invalid amount for deposit.")

    def test_deposit_negative_amount(self):
        account = BankAccount("12345", "John Doe", 100)
        self.assertEqual(account.deposit(-20), "Invalid amount for deposit.")

    def test_withdraw_valid_amount(self):
        account = BankAccount("12345", "John Doe", 200)
        self.assertEqual(account.withdraw(150), "Withdrew $150. New balance: $50")

    def test_withdraw_insufficient_balance(self):
        account = BankAccount("12345", "John Doe", 100)
        self.assertEqual(account.withdraw(200), "Insufficient funds or invalid amount for withdrawal.")

    def test_withdraw_zero_amount(self):
        account = BankAccount("12345", "John Doe", 100)
        self.assertEqual(account.withdraw(0), "Insufficient funds or invalid amount for withdrawal.")

    def test_withdraw_negative_amount(self):
        account = BankAccount("12345", "John Doe", 100)
        self.assertEqual(account.withdraw(-50), "Insufficient funds or invalid amount for withdrawal.")

    def test_display_balance(self):
        account = BankAccount("12345", "John Doe", 300)
        self.assertEqual(account.display_balance(), "Current Balance: $300")

# This will run the test when the script is run (normally).
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
