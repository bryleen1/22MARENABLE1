class Budget:
    def __init__(self, balance):
        self.balance = balance

    def __repr__(self):
        print(f"Your budget for the month is £{self.balance}") 

    def deposit(self, money):
        self.balance = self.balance + money
        print(f"The balance is: {self.balance}")

    def withdraw(self, money):
        self.balance = self.balance - money
        print(f"The balance is: {self.balance}")