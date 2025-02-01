#Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. 
#Withdrawals may not exceed the available balance. 
#Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class PrimeFilter:
    def prime(num):
        if num <= 1:
            return False
        elif num == 2:
            return True
        elif num % 2 == 0:
            return False
        else:
            for i in range(3, int(num**0.5) + 1, 2):
                if num % i == 0:
                    return False
            return True

    def filter(self, nums):
        return list(filter(lambda x:self.prime(x), nums))