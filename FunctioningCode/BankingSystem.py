from Employee import Employee
from Customer import Customer
from Account import Account
import Log

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

# gives user two choices log-in or sign-up


def customerChoice():
    CustomerChoice_input = None
    while CustomerChoice_input != "1" or CustomerChoice_input != "2":
        CustomerChoice_input = input("Please choose (1)'log_in' or (2)'sign_up': ")
        if CustomerChoice_input == "1":
            custLogIn()
            chooseActivity()
        elif CustomerChoice_input == "2":
            signUp()
            chooseActivity()
        else:
            print("Please choose option 1 or 2")


def custLogIn():
    customerID = None
    while True:
        customerID = input("Customer ID: ")
        if checkCustID_exists(customerID):
            break
    customer = createCustomerObject(customerID)
    # in this function make sure the input is valid


def createCustomerObject(ID):
    with open("/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Database/Customers.json", 'r') as custf:
        file_dict = json.load(custf)
        for c in file_dict["customers"]:
            if c["customer_id"] == ID:
               return Customer(c["customer_id"], c["name"], c["ssn"], c["address"], c["age"], c["creditScore"])

def checkCustID_exists(ID):
    with open("/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Database/Customers.json", 'r') as custf:
        file_dict = json.load(custf)
        for customer in file_dict["Customers"]:
            if customer["customer_id"] == ID:
                return True
        return False 

def signUp():
    customerID = None
    while True:
        customerID = input("Customer ID: ")
        if not checkCustID_exists(customerID):
            break
        Log.warning("Customer already exists","/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Logs/")
    name = getName()
    ssn = getSSN()
    checkings_bal = getCheckingsBal()
    savings_bal = getCheckingsBal()
    address = getAddress()
    age = getAge()
    creditScore = input("Credit Score: ")
    # check all inputs

    customer = Customer(customerID, name, ssn, address, age, creditScore)
    customer.write_to_db()
    account = Accounts(checkings_bal, savings_bal)
    account.write_accounts_to_db()
    # create accounts in db

def getName():
    name = None
    while True:
        name = input("Name: ") #isnumeric() , isalphanumeric()), isalpha()
        if not name.isalpha():
            Log.warning("Must be alpha...",'/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Logs/')
            continue
        if len(name) < 2:
            Log.warning("Must be longer than 2 characters",'/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Logs/')
            continue
        break
    return name

def getSSN():
    ssn = None
    while True:
        ssn = input("Social Security #: ") #isnumeric() , isalphanumeric()), isalpha()
        if not ssn.isnumeric():
            Log.warning("Must be numeric...",'/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Logs/')
            continue
        if len(ssn) != 6:
            Log.warning("Must be 6 characters",'/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Logs/')
            continue
        break
    return ssn

def getCheckingsBal():
    CheckingBal = None
    while True:
        CheckingBal = input("Checking Bal: ") #isnumeric() , isalphanumeric()), isalpha()
        if not CheckingBal.isnumeric():
            Log.warning("Must be numeric...",'/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Logs/')
            continue
        if CheckingBal < 0:
            Log.warning("Cant be a negative number...",'/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Logs/')
            continue
        break
    return ChekingBal

def getSavingsBal():
    SavingsBal = None
    while True:
        SavingsBal = input("Savings Bal: ") #isnumeric() , isalphanumeric()), isalpha()
        if not SavingsBal.isnumeric():
            Log.warning("Must be numeric...",'/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Logs/')
            continue
        if SavingsBal < 0:
            Log.warning("Cant be a negative number...",'/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Logs/')
            continue
        break
    return SavingsBal

def getAddress():
    address = None
    while True:
        address = input("Address: ") #isnumeric() , isalphanumeric()), isalpha()
        if not address.isalphanumeric():
            Log.warning("Must be alphanumeric...",'/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Logs/')
            continue
        if len(address) < 6:
            Log.warning("Address must be longer than 6 charcters...",'/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Logs/')
            continue
        break
    return address

def getAge():
    age = None
    while True:
        age = input("Age: ") #isnumeric() , isalphanumeric()), isalpha()
        if not age.isnumeric():
            Log.warning("Must be numeric...",'/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Logs/')
            continue
        if age < 18:
            Log.warning("Must be 18 or older to sign up...",'/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Logs/')
            continue
        break
    return age

def getCreditScore():
    CreditScore = None
    while True:
        CreditScore = input("CreditScore: ") #isnumeric() , isalphanumeric()), isalpha()
        if not CreditScore.isnumeric():
            Log.warning("Must be numeric...",'/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Logs/')
            continue
        if CreditScore < 300 and CreditScore > 850:
            Log.warning("Credit score must be between 300 and 850 ...",'/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Logs/')
            continue
        break
    return CreditScore


def employeeChoice():
    empLogIn()
    showPendingRequests(employee.department)
    #loop thru the returned pending requests and call request decision on each request
    for request in PendingRequests:
        requestDecision(request)

def empLogIn():
    employeeID = None
    while True:
        employeeID = input("Employee ID: ")
        if checkEmpID_exists(employeeID):
            break
    # in this function make sure the input is valid
    employee = createEmployeeObject(employeeID)

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
            if request["departrment"] == employee["department"]:
                PendingRequests.append(request)
        return PendingRequests 

def requestDecision(request):
    # print pending requests for the logged in user
    # print an option to approve or deny each request
    approveOrDeny_input = None
    while approveOrDeny_input != "1" or approveOrDeny_input != "2":
        approveOrDeny_input = input("Please choose (1)'approve' or (2)'deny': ")
        if approveOrDeny_input == "1":
            # log approval in ServiceHistory.text
            with open("/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Database/ServiceHistory.txt", 'a') as historyf:
                historyf.write(f'Request {request.request_id} has been approved'
            # delete request from pending requests
            deleteRequest()
        elif approveOrDeny_input == "2":
            # log denial in ServiceHistory.text
            with open("/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Database/ServiceHistory.txt", 'a') as historyf:
                historyf.write(f'Request {request.request_id} has been declined')
            # delete request from pending requests
            deleteRequest()
        else:
            print("Please choose option 1 or 2")
    
def deleteRequest():
    with open("/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Database/PendingRequests.json", 'r') as requestf:
            file_dict = json.load(requestf)
            for index, request in enumerate(file_dict["Requests"]):
                del file_dict["Requests"][index]
                with open("/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Database/PendingRequests.json", 'w') as requestf:
                    json.dump(file_dict,requestf)



def chooseActivity():
    ActivityChoice_input = None
    while ActivityChoice_input != "1" or ActivityChoice_input != "2":
        ActivityChoice_input = input(
            "Please choose (1)'Accounts Summary' or (2)'Use Service': ")
        if ActivityChoice_input == "1":
            pass
            # accountsSummary()
        elif ActivityChoice_input == "2":
            pass
            # useService()
        else:
            print("Please choose option 1 or 2")


def accountsSummary(ID):
    # for the user print the account id, account type, and account balance for each account

    # allow the user to choose either their checking or savings acct
    AccountChoice_input = None
    while AccountChoice_input != "1" or AccountChoice_input != "2":
        AccountChoice_input = input("Please choose (1)'Ckeckings Account' or (2)'Savings Account': ")
        if AccountChoice_input == "1":
            # checkingsChoice()
        elif AccountChoice_input == "2":
            # savingsChoice()
        else:
            print("Please choose option 1 or 2")

def checkingsChoice()

# if checkings account the user can choose either deposit or withdrawl
AccountChoice_input = None
   while AccountChoice_input != "1" or AccountChoice_input != "2":
        AccountChoice_input = input(
            "Please choose (1)'Deposit' or (2)'Withdrawl': ")
        if AccountChoice_input == "1":
            # deposit()
        elif AccountChoice_input == "2":
            # withdrawl()
        else:
            print("Please choose option 1 or 2")


def savingsChoice()

# if Savings account the user can choose Deposit or transfer
AccountChoice_input = None
   while AccountChoice_input != "1" or AccountChoice_input != "2":
        AccountChoice_input = input(
            "Please choose (1)'Deposit' or (2)'Transfer': ")
        if AccountChoice_input == "1":
            # deposit()
        elif AccountChoice_input == "2":
            # transfer()
        else:
            print("Please choose option 1 or 2")


def useService():
    # allow user to choose apply for loan or apply for credit card
    ServiceChoice_input = None
    while ServiceChoice_input != "1" or ServiceChoice_input != "2":
        ServiceChoice_input = input(
            "Please choose (1)'Apply for Loan' or (2)'Apply for Credit Card': ")
        if ServiceChoice_input == "1":
            # applyForLoan()
        elif AccountChoice_input == "2":
            # applyForCreditCard()
        else:
            print("Please choose option 1 or 2")


def applyForLoan()
   # approve loan if they have over 50,000 in savings account decline if under
            # if declined give them the option to set an employee meeting


def applyForCreditCard()

   # approve credit card if they have credit score over 600 decline if under
           # if declined give them the option to set an employee meeting
startProgram()
