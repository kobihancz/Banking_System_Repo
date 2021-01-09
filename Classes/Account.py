import json

class Account:
    def __init__(self,customer_id, balance):
       self.balance = balance
       self.customer_id = customer_id
    
    def deposit(self, atype, amount):
        self.balance = self.balance + amount 
        return self.balance
    
    #update account w/ customer method --> customer.py
    def update_AccountBalance(self, atype, newbalance):
        with open("/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Database/Accounts.json", 'r') as acctf:
            file_dict = json.load(acctf)
            for acct in file_dict["Accounts"]:
                if "customer_id" in acct and acct["customer_id"] == self.customer_id and acct["account_type"] == atype:
                    acct["balance"] = newbalance
                with open("/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Database/Accounts.json", 'w') as testf:
                    json.dump(file_dict,testf)
                   

    def write_accounts_to_db(self, atype):
        with open("/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Database/Accounts.json", 'r') as accountf:
            file_dict = json.load(accountf)
            temp = self.__dict__
            temp['account_type'] = atype
            file_dict["Accounts"].append(temp)
        with open("/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Database/Accounts.json", 'w') as accountf:
            json.dump(file_dict,accountf)

class Checking(Account):
    def __init__(self,customer_id, balance):
        self.balance = balance
        self.customer_id = customer_id 

    def withdrawl(self, atype, amount):
        self.balance = self.balance - amount 
        return self.balance

class Saving(Account):
    def __init__(self,customer_id, balance):
        self.balance = balance
        self.customer_id= customer_id

    def transfer(self, amount, checkings):
        self.balance = self.balance - amount
        checkings.balance = checkings.balance + amount
        return self.balance, checkings.balance

         