import logging

logging.basicConfig(level=logging.INFO)

class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initial_amount, acct_name):
        if initial_amount < 0:
            raise ValueError("Initial amount cannot be negative.")
        self.name = acct_name
        self.balance = initial_amount
        self.history = []  # To track transaction history
        logging.info(f"Account Name: {self.name} created with balance: ${self.balance}.")

    def get_balance(self):
        logging.info(f"Account '{self.name}' Balance: ${self.balance}")
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        self.history.append(f"Deposited: ${amount}")
        logging.info("Deposit complete.")
        self.get_balance()

    def _is_transaction_valid(self, amount):
        if amount > self.balance:
            raise BalanceException(f"Insufficient funds in account '{self.name}'. Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        try:
            self._is_transaction_valid(amount)
            self.balance -= amount
            self.history.append(f"Withdrew: ${amount}")
            logging.info("Withdrawal completed.")
            self.get_balance()
        except BalanceException as error:
            logging.error(f"Withdrawal interrupted: {error}")

    def show_history(self):
        logging.info(f"Transaction History for '{self.name}':")
        for record in self.history:
            logging.info(record)
