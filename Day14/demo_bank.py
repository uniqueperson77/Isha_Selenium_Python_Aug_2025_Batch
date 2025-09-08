class Bank:
    def __init__(self,acnt_num,balance):
        self.account_number = acnt_num
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance+amount
        print("Amount of {} deposited".format(amount))
        print("Updated balance: {}".format(self.balance))


    def withdraw(self,withdraw_amount):
        if withdraw_amount>self.balance:
            print("trying to withdraw amount higher than balance.")
            print("")
        else:
            self.balance = self.balance - withdraw_amount
            print("Amount of {} waithdrawn".format(withdraw_amount))
            print("Updated balance: {}".format(self.balance))

    def check_balance(self):
        print("Current balance: "+ str(self.balance))


bean = Bank("100200300",2000)
sachin = Bank(acnt_num="200300500",balance=0)
# print(obj)
# print(obj.balance)
# obj.check_balance()
# print(obj.account_number)
bean.deposit(6000)
sachin.deposit(1000)
# bean.check_balance()
# bean.withdraw(9000)


Bank("100200300",2000).deposit(1000)