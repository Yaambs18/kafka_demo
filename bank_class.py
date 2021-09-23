class Account():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, deposit_amount):
        print("Deposit Accepted")
        self.balance += deposit_amount
    
    def withdraw(self, withdraw_amount):
        if withdraw_amount <= self.balance:
            print("Withdrawal Accepted")
            self.balance -= withdraw_amount
        else:
            print("Funds Unavailable!")

    def __str__(self):
        return f"Account owner : {self.owner} \nAccount balance : {self.balance}"

acct1 = Account('Jose',1000)
Transactions = {"Owner": acct1.owner, "deposit1": acct1.deposit(50), "withdraw1": acct1.withdraw(75), "withdraw2": acct1.withdraw(500), "Clear Balance": acct1.balance}
     