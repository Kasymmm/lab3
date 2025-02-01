#Create a bank account class that has attributes owner, balance and two methods deposit and withdraw.
#Withdrawals may not exceed the available balance. 
#Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account():
    def _init_(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print("Your balance now:", self.balance)
        else:
            pass

    def withdraw(self, draw):
        self.balance -= draw
        print("Your balance now:", self.balance)

account = Account("Name", 1000)
print("Summ of transition:")
i = int(input())
account.deposit(i)
print("Pay the draw:")
y = int(input())
account.withdraw(y)