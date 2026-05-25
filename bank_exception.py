class InsufficientFunds(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance=balance

    def withdraw(self,amount):
        if amount > self.balance:
            raise InsufficientFunds ("Insufficient funds in the account.")
        self.balance -= amount
        print(f"Withdrawal successful, remaining balance: {self.balance}")

try: 
    account = BankAccount(100)
    account.withdraw(150)

except InsufficientFunds as e:
    print("Transactions Failed:", e)