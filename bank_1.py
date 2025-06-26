class BalanceException(Exception):
    pass
class BankAccount:
    def __init__(self,initialAmount,acctName):
        self.name=acctName
        self.balance =initialAmount
        print(f"Account Name:: {self.name} created.")
        print(f"Balance ::${self.balance}\n")

    def getBalance(self):
        print(f"\n Account '{self.name} Balance=${self.balance}") 

    def deposit(self,amount):
        self.balance=self.balance + amount
        print("\n Deposit complete.")
        self.getBalance()

    def valueableTransaction(self,amount):
        if(amount <= self.balance):
            self.balance=self.balance - amount
            return 
        else:
            raise BalanceException(
                f"\n Sorry account'{self.name}' only has a balnace of ${self.balance}"
            )
        
    def withdraw(self,amount):
        try:
            self.valueableTransaction(amount)
            # self.balance=self.balance - amount   
            print(f"\n withdraw is completd.")
            self.getBalance()
        except BalanceException as error:
            print(f'\n Withdraw interrupted :{error}')

        
            

        