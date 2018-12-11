class BankAcount():
    def __init__(self, _balance=0):
        self._balance = _balance
    def deposit(self, _balance):
        self._balance += _balance
    def withdraw(self, _balance):
        if self._balance >_balance:
            self._balance -=_balance
            return _balance
        else:
            return "Insufficient funds"
BankAcount.deposit(input(print("Please enter a deposit")))

















