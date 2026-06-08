class Bankaccount:

    def __init__(self,account_number,balance,owner_name,date_opened):
        self.account_number=account_number
        self.balance=balance
        self.owner_name=owner_name
        self.date_opened=date_opened

    def deposit(self,date):
        print(f"{self.owner_name} deposited on {date} ")

    def withdraw(self,amount):
        print(f"{self.owner_name} withdraws {amount}")

    def check_balance(self,frequency):
        print(f"{self.owner_name} checks balance {frequency}")

    def display_info(self,method):
        print(f"account number{self.account_number} displays info {method}")

    def close_account(self,reason):
        print(f"{self.owner_name} closed account {reason}")

    def get_details(self):
        print(f"Name:{self.owner_name} -Account Number:{self.account_number} -Balance:{self.balance} -Date Opened:{self.date_opened}")
        print("----------------------------------------------------------------------------------------------")

# object1

account1=Bankaccount(400765,300000,"Alex","2023-04-01")
print(type(account1))
print(account1)
account1.get_details()
account1.deposit("2025-05-05")
account1.withdraw(10000)
account1.check_balance("Every week")
account1.display_info("via email")
account1.close_account("because of too many bank accounts")
# object2

account2=Bankaccount(400874,305000,"Mary","2022-01-01")
print(type(account2))
print(account2)
account2.get_details()
account2.deposit("2024-07-05")
account2.withdraw(10000)
account2.check_balance("Every weekend")
account2.display_info("via sms")
account2.close_account("because she lost her job")


