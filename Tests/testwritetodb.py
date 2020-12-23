import json
import sys
sys.path.append('/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Classes/')
from Customer import Customer
sys.path.append('/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Utilities/')
import Log


# def custLogIn():
#     customerID = None
#     while True:
#         customerID = input("Customer ID: ")
#         if checkCustID_exists(customerID):
#             break
#     customer = createCustomerObject(customerID)
#     print(customer)
#     # in this function make sure the input is valid

# def checkCustID_exists(ID):
#     with open("/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Database/Customers.json", 'r') as custf:
#         file_dict = json.load(custf)
#         for customer in file_dict["Customers"]:
#             if customer["customer_id"] == ID:
#                 return True
#         return False

# def createCustomerObject(ID):
#     with open("/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Database/Customers.json", 'r') as custf:
#         file_dict = json.load(custf)
#         for c in file_dict["Customers"]:
#             if c["customer_id"] == ID:
#                return Customer(c["customer_id"], c["name"], c["ssn"], c["address"], c["age"], c["creditScore"]) 

def getName():
    name = None
    while True:
        name = input("Name: ")
        if not name.isalpha():
            Log.warning("Must be alpha...",'/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Logs/')
            continue
        if len(name) < 2:
            Log.warning("Must be longer than 2 characters",'/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Logs/')
            continue
        break
    return name

getName()
# custLogIn()