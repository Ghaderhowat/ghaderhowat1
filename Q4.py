class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into {self.account_number}. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from {self.account_number}. New balance: {self.balance}")
        else:
            print(f"Insufficient funds in {self.account_number}.")

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        print(f"Applied {self.interest_rate * 100}% interest to {self.account_number}. New balance: {self.balance}")

    def __str__(self):
        return f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder}\nBalance: {self.balance}\nInterest Rate: {self.interest_rate * 100}%"

# Create an instance of BankAccount
bank_account = BankAccount("123456789", "John Doe")

# Perform a deposit and withdrawal
bank_account.deposit(1000)
bank_account.withdraw(500)

# Create an instance of SavingsAccount
savings_account = SavingsAccount("987654321", "Jane Smith", 0.05)

# Apply interest and print the account information
savings_account.apply_interest()
print(savings_account)