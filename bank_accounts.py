class BalanceException(Exception):
    pass
class BankAccount:
    def __init__(self, InitalAmount, accName):
        self.balance = InitalAmount
        self.name = accName
        print(f"Account '{self.name}' created. Balance = ${self.balance}")
    def getBalance(self):
        print(f"Account '{self.name}' balance = ${self.balance}")
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposit Complete!")
        self.getBalance()
    def viableTransaction(self, amount ):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"Sorry, the account '{self.name}' only has a balance of ${self.balance:.3f} in the account."
            )
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("Withdraw Complete! \nThank you for working with us, sir/ma'am.")
            self.getBalance()
        except BalanceException as error:
            print(f"Withdraw interrupted: \n {error}")

    def transfer(self, amount, account):
        try:
            print(f"\n*************\nBEGINNING THE TRANSFER...🚀...please wait 😊")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f"\nTransfer Complete!\n You have withdrawn ${amount} successfully. Congratulations!✅")

        except BalanceException as error:
            print(f"\nTransfer Interrupted!! ❌{error}")

class InterestRewards(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print(f"\nDeposit Compeleted!")
        print("balance after deposit: ", self.getBalance())

class SavingsAcccount(InterestRewards):
    def __init__(self, initialAmount, accName):
        super().__init__(initialAmount, accName)
        self.fee = 5

    def withdraw(self, amount): #overriding the Parent class's withdrawing method with a new
        try:
            self.viableTransaction(amount, self.fee)
            self.balance = self.balance - (amount + self.fee)
            print(f"\nWithdraw Compelete!")
            self.getBalance()
        except BalanceException as error:
             print(f'Withdraw Interrupted: {error}')

