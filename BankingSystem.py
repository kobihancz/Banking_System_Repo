from Classes.Employee import Employee
from Classes.Customer import Customer
from Classes.Account import Account,Checking,Saving
from Classes.Service import Service
from Utilities.Log import * 
import json

# starts program giving the user two choice sequences. Customer or Employee


def startProgram():
    UserChoice_input = None
    while UserChoice_input != "Customer" or UserChoice_input != "customer" or UserChoice_input != "Employee" or UserChoice_input != "employee":
        UserChoice_input = input("Please choose 'Customer' or 'Employee': ")
        if UserChoice_input == "Customer" or UserChoice_input == "customer":
            customerChoice()
        elif UserChoice_input == "Employee" or UserChoice_input == "employee":
            employeeChoice()
        else:
            print("Please choose a valid user choice.")

# gives customer user two choices log-in or sign-up


def customerChoice():
    CustomerChoice_input = None
    while CustomerChoice_input != "1" or CustomerChoice_input != "2":
        CustomerChoice_input = input(
            "Please choose (1)'log_in' or (2)'sign_up': ")
        if CustomerChoice_input == "1":
            user_dict = custLogIn()
            chooseActivity(user_dict)
        elif CustomerChoice_input == "2":
            user_dict = signUp()
            chooseActivity(user_dict)
        else:
            print("Please choose option 1 or 2")

# user inputs ID, input is checked, 3 objects are created and put into  a dictionary. This dictionary will be passed through the rest of the program


def custLogIn():
    customerID = None
    while True:
        customerID = int(input("Customer ID: "))
        if checkCustID_exists(customerID):
            break
    customer = createCustomerObject(customerID)
    checkings = createCheckingAcctObject(customerID)
    savings = createSavingsAcctObject(customerID)
    return {"customer": customer, "checkings": checkings, "savings": savings}

# check if ID exists in Customer db


def checkCustID_exists(ID):
    with open("/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Database/Customers.json", 'r') as custf:
        file_dict = json.load(custf)
        for customer in file_dict["Customers"]:
            if customer["customer_id"] == ID:
                return True
        return False

# creates Customer object fron Customers db


def createCustomerObject(ID):
    with open("/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Database/Customers.json", 'r') as custf:
        file_dict = json.load(custf)
        for c in file_dict["Customers"]:
            if c["customer_id"] == ID:
               return Customer(c["customer_id"], c["name"], c["ssn"], c["address"], c["age"], c["creditScore"])

# creates Checking object from Accounts db


def createCheckingAcctObject(ID):
    with open("/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Database/Accounts.json", 'r') as acctf:
        file_dict = json.load(acctf)
        for a in file_dict["Accounts"]:
            if a["customer_id"] == ID and a["account_type"] == "checkings":
               return Checking(a["customer_id"], a["balance"])

# creates Savings Object from Accounts db


def createSavingsAcctObject(ID):
    with open("/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Database/Accounts.json", 'r') as acctf:
        file_dict = json.load(acctf)
        for a in file_dict["Accounts"]:
            if a["customer_id"] == ID and a["account_type"] == "savings":
               return Saving(a["customer_id"], a["balance"])

# User inputs ID, input is checked, Customer info is inputed by the customer, 3 objects are created from the inputs and put into  a dictionary. This dictionary will be passed through the rest of the program


def signUp():
    customerID = None
    while True:
        customerID = int(input("Customer ID: "))
        if not checkCustID_exists(customerID):
            break
        warning("Customer already exists",
                    "/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Logs/")
    name = getName()
    ssn = getSSN()
    checkings_bal = getCheckingsBal()
    savings_bal = getSavingsBal()
    address = getAddress()
    age = getAge()
    creditScore = getCreditScore()

    customer = Customer(customerID, name, ssn, address, age, creditScore)
    customer.write_customer_to_db()
    checkings = Checking(customerID, checkings_bal)
    checkings.write_accounts_to_db("checkings")
    savings = Saving(customerID, savings_bal)
    savings.write_accounts_to_db("savings")

    return {"customer": customer, "checkings": checkings, "savings": savings}


def getName():
    name = None
    while True:
        name = input("Name: ")  # isnumeric() , isalphanumeric()), isalpha()
        if not name.isalpha():
            warning(
                "Must be alpha...", '/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Logs/')
            continue
        if len(name) < 2:
            warning("Must be longer than 2 characters",
                        '/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Logs/')
            continue
        break
    return name


def getSSN():
    ssn = None
    while True:
        # isnumeric() , isalphanumeric()), isalpha()
        ssn = input("Social Security #: ")
        if not ssn.isnumeric():
            warning("Must be numeric...",
                        '/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Logs/')
            continue
        if len(ssn) != 6:
            warning("Must be 6 characters",
                        '/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Logs/')
            continue
        break
    return ssn


def getCheckingsBal():
    CheckingBal = None
    while True:
        # isnumeric() , isalphanumeric()), isalpha()
        CheckingBal = int(input("Checking Bal: "))
        if CheckingBal < 0:
            warning("Cant be a negative number...",
                        '/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Logs/')
            continue
        break
    return CheckingBal


def getSavingsBal():
    SavingsBal = None
    while True:
        # isnumeric() , isalphanumeric()), isalpha()
        SavingsBal = int(input("Savings Bal: "))
        if SavingsBal < 0:
            warning("Cant be a negative number...",
                        '/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Logs/')
            continue
        break
    return SavingsBal


def getAddress():
    address = None
    while True:
        # isnumeric() , isalphanumeric()), isalpha()
        address = input("Address: ")
        if len(address) < 6:
            warning("Address must be longer than 6 charcters...",
                        '/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Logs/')
            continue
        break
    return address


def getAge():
    age = None
    while True:
        age = int(input("Age: "))  # isnumeric() , isalphanumeric()), isalpha()
        if age < 18:
            warning("Must be 18 or older to sign up...",
                        '/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Logs/')
            continue
        break
    return age


def getCreditScore():
    CreditScore = None
    while True:
        # isnumeric() , isalphanumeric()), isalpha()
        CreditScore = int(input("CreditScore: "))
        if CreditScore < 300 or CreditScore > 850:
            warning("Credit score must be between 300 and 850 ...",
                        '/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Logs/')
            continue
        break
    return CreditScore


def employeeChoice():
    employee = empLogIn()
    requests = showPendingrequests(employee.department)
    # loop thru the returned pending requests and call request decision on each request
    for request in requests:
        print(request)
        requestDecision(request)
        deleteRequests(employee.department)
        print(f'Request {request["request_ID"]} has been deleted')
    print(f'All requests have been processed in the {employee.department} department')

def empLogIn():
    employeeID = None
    while True:
        employeeID = int(input("Employee ID: "))
        if checkEmpID_exists(employeeID):
            break
    # in this function make sure the input is valid
    return createEmployeeObject(employeeID)


def checkEmpID_exists(ID):
    with open("/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Database/Employees.json", 'r') as empf:
        file_dict = json.load(empf)
        for employee in file_dict["Employees"]:
            if employee["employee_id"] == ID:
                return True
        return False


def createEmployeeObject(ID):
    with open("/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Database/Employees.json", 'r') as custf:
        file_dict = json.load(custf)
        for e in file_dict["Employees"]:
            if e["employee_id"] == ID:
               return Employee(e["employee_id"], e["name"], e["department"])


def showPendingrequests(department):
    PendingRequests = []
    with open("/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Database/PendingRequests.json", 'r') as requestf:
        file_dict = json.load(requestf)
        for request in file_dict["Requests"]:
            if request["department"] == department:
                PendingRequests.append(request)
        return PendingRequests


def requestDecision(request):
    # print an option to approve or deny each request
    approveOrDeny_input = None
    while approveOrDeny_input != "1" or approveOrDeny_input != "2":
        approveOrDeny_input = input(
            "Please choose (1)'approve' or (2)'deny': ")
        if approveOrDeny_input == "1":
            # log approval in ServiceHistory.text
            with open("/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Database/ServiceHistory.txt", 'a') as historyf:
                historyf.write(
                    f'Request {request["request_ID"]} has been approved'+'\n')
                break
            # delete request from pending requests
        elif approveOrDeny_input == "2":
            # log denial in ServiceHistory.text
            with open("/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Database/ServiceHistory.txt", 'a') as historyf:
                historyf.write(
                    f'Request {request["request_ID"]} has been declined' + '\n')
                break
            # delete request from pending requests
        else:
            print("Please choose option 1 or 2")


def deleteRequests(department):
    with open("/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Database/PendingRequests.json", 'r') as requestf:
        file_dict = json.load(requestf)
        for index, request in enumerate(file_dict["Requests"]):
            if file_dict['Requests'][index]['department'] == department:
                file_dict["Requests"].pop(index)
            with open("/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Database/PendingRequests.json", 'w') as requestf:
                json.dump(file_dict, requestf)


def chooseActivity(user_dict):
    ActivityChoice_input = None
    while ActivityChoice_input != "1" or ActivityChoice_input != "2":
        ActivityChoice_input = input(
            "Please choose (1)'Accounts Summary' or (2)'Use Service': ")
        if ActivityChoice_input == "1":
            pass
            accountsSummary(user_dict)
        elif ActivityChoice_input == "2":
            pass
            useService(user_dict)
        else:
            print("Please choose option 1 or 2")


def accountsSummary(user_dict):

   # for the user print the, account type, and account balance for each account
    print("CHECKINGS:")
    print("CustomerID - " + str(user_dict["checkings"].customer_id))
    print("Balance - " + str(user_dict["checkings"].balance))
    print("SAVINGS:")
    print("CustomerID - " + str(user_dict["savings"].customer_id))
    print("Balance - " + str(user_dict["savings"].balance))
   # allow the user to choose either their checking or savings acct
    AccountChoice_input = None
    while AccountChoice_input != "1" or AccountChoice_input != "2":
        AccountChoice_input = input(
            "Please choose (1)'Ckeckings Account' or (2)'Savings Account': ")
        if AccountChoice_input == "1":
            checkingsChoice(user_dict)
            break
        elif AccountChoice_input == "2":
            savingsChoice(user_dict)
            break
        else:
            print("Please choose option 1 or 2")


def checkingsChoice(user_dict):
# if checkings account the user can choose either deposit or withdrawl
    AccountChoice_input = None
    while AccountChoice_input != "1" or AccountChoice_input != "2":
        AccountChoice_input = input(
            "Please choose (1)'Deposit' or (2)'Withdrawl': ")
        if AccountChoice_input == "1":
            # deposit
            amount = int(input("Please enter a Deposit amount: "))
            newbalance=user_dict["checkings"].deposit("checkings", amount)
            user_dict["checkings"].update_AccountBalance("checkings", newbalance)
            print(f'Checkings account deposit of {amount} has been made')
        elif AccountChoice_input == "2":
            # withdrawl
            amount=int(input("Please enter a Withdrawl amount: "))
            newbalance=user_dict["checkings"].withdrawl("checkings", amount)
            user_dict["checkings"].update_AccountBalance("checkings", newbalance)
            print(f'Checkings account withdrawl of {amount} has been made')
        else:
            print("Please choose option 1 or 2")

def savingsChoice(user_dict):
# if Savings account the user can choose Deposit or transfer
    AccountChoice_input=None
    while AccountChoice_input != "1" or AccountChoice_input != "2":
        AccountChoice_input=input(
            "Please choose (1)'Deposit' or (2)'Transfer': ")
        if AccountChoice_input == "1":
            # deposit
            amount = int(input("Please enter a Deposit amount: "))
            newbalance=user_dict["savings"].deposit("savings", amount)
            user_dict["savings"].update_AccountBalance("savings", newbalance)
            print(f'Savings account deposit of {amount} has been made')
            break
        elif AccountChoice_input == "2":
            # transfer
            amount=int(input("Please enter a Transfer amount: "))
            newBalTuple=user_dict["savings"].transfer(
                amount, user_dict["checkings"])
            user_dict["savings"].update_AccountBalance("savings",newBalTuple[0])
            user_dict["checkings"].update_AccountBalance("checkings",newBalTuple[1])
            print(f'Transfer of {amount} has been made')
            break
        else:
            print("Please choose option 1 or 2")

def useService(user_dict):
    # allow user to choose apply for loan or apply for credit card
    ServiceChoice_input=None
    while ServiceChoice_input != "1" or ServiceChoice_input != "2":
        ServiceChoice_input=input(
            "Please choose (1)'Apply for Loan' or (2)'Apply for Credit Card': ")
        if ServiceChoice_input == "1":
            applyForLoan(user_dict)
            break
        elif ServiceChoice_input == "2":
            applyForCreditCard(user_dict)
            break
        else:
            print("Please choose option 1 or 2")


def applyForLoan(user_dict):
    # create a service object from user_dict
    request = Service(user_dict["customer"].customer_id, user_dict["customer"].name,
                    user_dict["savings"].balance, user_dict["customer"].creditScore, "Loan")
    # approve or decline based on if they have over 50,000 in savings
    decision=request.approve_or_decline_loan()
    # if approved add to serviceHistory
    if decision == True:
        request.write_service_to_history()
    # if declined add it to the requests database
    else:
        request.write_request_to_db()


def applyForCreditCard(user_dict):
    # create a service object from user_dict and add it to the requests database
    request = Service(user_dict["customer"].customer_id, user_dict["customer"].name,
                    user_dict["savings"].balance, user_dict["customer"].creditScore, "CreditCard")
    # approve or decline based on if they have credit score over 600
    decision = request.approve_or_decline_creditCard()
    # if approved add to serviceHistory
    if decision == True:
        request.write_service_to_history()
    # if declined add it to the request db
    else:
        request.write_request_to_db()

startProgram()