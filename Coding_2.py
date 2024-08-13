class Account:
    def __init__(self,owner,amount):
        self.owner = owner
        self.amount = amount

    def __str__(self):
        return f"Account owner:{self.owner}\nBalance:{self.amount}"
    
    def deposit(self,dep):
         self.amount = self.amount + dep
    
    def withdraw(self,wit):
        if wit>self.amount:
            return "funds Unavailable"
        else:
            self.amount-=wit
            

acc1 = Account('Jose',100)
acc1.deposit(50)
print(acc1.withdraw(300))
print(acc1)