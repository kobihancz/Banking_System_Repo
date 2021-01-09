import json


class Customer:
    #intit function to accept the inputed data in banking system.py and create a customer object
    #write customer to db function to add inputed customer to database 
    #check if Customer id is in database function
    #write accounts to db


    def __init__(self, customerID, name , ssn, address, age, creditScore):
        self.customer_id =  customerID
        self.ssn = ssn
        self.name = name
        self.address = address
        self.age = age 
        self.creditScore = creditScore
        # If something is missing, throw error /specify thast missing attr

    def write_customer_to_db(self):
        with open("/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Database/Customers.json", 'r') as custf:
            file_dict = json.load(custf)
            file_dict["Customers"].append(self.__dict__)
        with open("/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Database/Customers.json", 'w') as testf:
            json.dump(file_dict,testf)

    # def update_CustomerAddress(self,newaddress):
    #     with open("/Users/kobihancz/Desktop/Finance_Project/Database/customerstest.json", 'r') as custf:
    #         file_dict = json.load(custf)
    #         for cust in file_dict["Customers"]:
    #             if "customer_id" in cust and cust['customer_id'] == self.customer_id:
    #                 cust["address"] = newaddress
    #             with open("/Users/kobihancz/Desktop/Finance_Project/Database/customerstest.json", 'w') as testf:
    #                 json.dump(file_dict,testf)
    
    # def delete_customer_from_db(self):
    #     with open("/Users/kobihancz/Desktop/Finance_Project/Database/customerstest.json", 'r') as custf:
    #         file_dict = json.load(custf)
    #         for index, cust in enumerate(file_dict["Customers"]):
    #             del file_dict["Customers"][index]
    #             with open("/Users/kobihancz/Desktop/Finance_Project/Database/customerstest.json", 'w') as testf:
    #                 json.dump(file_dict,testf)
    
    # def read_customer_from_db(self):
    #     with open("/Users/kobihancz/Desktop/Finance_Project/Database/customerstest.json", 'r') as custf:
    #         file_dict = json.load(custf)
    #         for cust in file_dict["Customers"]:
    #             if "customer_id" in cust and cust["customer_id"]==self.customer_id:
    #                 print(cust)


