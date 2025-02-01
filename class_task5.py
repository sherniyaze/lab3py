# Create a bank account class that has attributes
# owner, balance and two methods deposit and withdraw. 
# Withdrawals may not exceed the available balance. 
# Instantiate your class, make several deposits and 
# withdrawals, and test to make sure the account 
# can't be overdrawn.



class bank_account():
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self):
        to_deposit = float(input())
        self.balance+=to_deposit
    def withdraw(self):
        how_much = float(input())
        if how_much<self.balance:
            self.balance-=how_much
            print(f"вы сняли {how_much} тенге со счета и на балансе осталось {self.balance} тенге")
        else: 
            print("у вас уважаемая бедолага не хватает средств на балансе")
            print(f"вы хотели снять {how_much} тенге")
            print(f"у вас на счету {self.balance} тенге")    
            print(f"вам не хватает{how_much - self.balance} тенге")

owner1 = input()
balance_of_owner1 = float(input())
owner1s_account = bank_account(owner1,balance_of_owner1)
owner1s_account.deposit()
owner1s_account.withdraw()
