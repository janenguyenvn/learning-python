class Account():
    def __init__(self,name, balance):
        self.name = name
        self.balance = balance
    def the_object(self):
        print('Account owner: ' + name)
        print('Account balance: ' + balance)
    def deposit(self,number):
        print('Deposit Accepted')
        self.balance += number
    def withdraw(self,withdraw_number):
        if withdraw_number > self.balance:
            print('Funds Unavailable!!!')
        else:
            print('Withdraw Accepted!!!')

acct1 = Account('Jose',100)
print(acct1.balance)
print(acct1.deposit(20))
print(acct1.balance)
print(acct1.withdraw(130))
