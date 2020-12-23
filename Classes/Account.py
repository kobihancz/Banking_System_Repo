#Checkings & Savings Accounts

#Methods – Withdraw & Deposit

class Account:
    def __init__(self, checkings_balance, savings_balance):
        self.checkings = Checking(checkings_balance)
        self.savings = Saving(savings_balance)
        
    
    def deposit(self, amount):
        #Deposit amount in account

    def write_accounts_to_db(self):
        with open("/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Database/Accounts.json", 'r') as accountf:
            file_dict = json.load(accountf)
            file_dict["Customers"].append(self.__dict__)
        with open("/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Database/Accounts.json", 'w') as accountf:
            json.dump(file_dict,accountf)

class Checking(Account):
    def __init__(self, balance):
        self.balance = balance 

    def withdrawl(self, amount):
        #Withdraw amount from account 

class Saving(Account):
    def __init__(self, balance):
        self.balance = balance 

    def transfer(self, amount, checkings_obj):
        checkings_obj.balance += amount 