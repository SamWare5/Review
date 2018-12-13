class BankAcount():
    balance = 0

    def __init__(self, input_balance):
        self.balance = input_balance


    def deposit(self, deposit_amount):
        self.balance += deposit_amount


    def withdraw(self, withdraw_amount):
        self.balance -= withdraw_amount


"""       
        if self._balance >_balance:
            self._balance -=_balance
            return _balance
        else:
            return "Insufficient funds"
"""


b = BankAcount(10)
b.deposit(25)
b.withdraw(1)
print("My actual balance is " + str(b.balance))



















