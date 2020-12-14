from Customer import Customer

#starts program giving the user two choice sequences. Customer or Employee
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

#gives user two choices log-in or sign-up      
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
    log_inCustomerid_input = input("Customer ID: ")
    #in this function make sure the input is valid

def signUp():
    customerID = input("Customer ID: ") 
    name  = input("Name: ")
    ssn  = input("Social Security #: ")
    checkings = input("Checking Balance: ")
    savings = input("savings Balance: ")
    address = input("Address: ")
    age = input("Age: ")
    creditScore = input("Credit Score: ")
    
    customer = Customer(customerID, name, ssn, address, age, creditScore)
   
    #create customer in db
    #create accounts in db 
    #check all inputs

#employee logs in using their employee ID
def employeeChoice():
    empLogIn()
    #showPendingRequests() 

def empLogIn():
    log_inEmployeeid_input = input("Employee ID: ")
    #in this function make sure the input is valid

def showPendingRequests():
    #print pending requests for the logged in user 
    #print an option to approve or deny each request 
    approveOrDeny_input = None
    while approveOrDeny_input != "1" or approveOrDeny_input != "2":
        approveOrDeny_input = input("Please choose (1)'approve' or (2)'deny': ")
        if approveOrDeny_input == "1":
            #log approval in ServiceHistory.text
        elif approveOrDeny_input == "2":
            #log denial in ServiceHistory.text
        else:
            print("Please choose option 1 or 2")

def chooseActivity():
    ActivityChoice_input = None
    while ActivityChoice_input != "1" or ActivityChoice_input != "2":
        ActivityChoice_input = input("Please choose (1)'Accounts Summary' or (2)'Use Service': ")
        if ActivityChoice_input == "1":
            pass
            #accountsSummary()
        elif ActivityChoice_input == "2":
            pass
            #useService()
        else:
            print("Please choose option 1 or 2") 

def accountsSummary():
    #for the user print the account id, account type, and account balance for each account 
    #allow the user to choose either their checking or savings acct
    AccountChoice_input = None
    while AccountChoice_input != "1" or AccountChoice_input != "2":
        AccountChoice_input = input("Please choose (1)'Ckeckings Account' or (2)'Savings Account': ")
        if AccountChoice_input == "1": 
            #checkingsChoice() 
        elif AccountChoice_input == "2":
            #savingsChoice()
        else:
            print("Please choose option 1 or 2")

def checkingsChoice() 
#if checkings account the user can choose either deposit or withdrawl
AccountChoice_input = None
    while AccountChoice_input != "1" or AccountChoice_input != "2":
        AccountChoice_input = input("Please choose (1)'Deposit' or (2)'Withdrawl': ")
        if AccountChoice_input == "1": 
            #deposit()
        elif AccountChoice_input == "2":
            #withdrawl()
        else:
            print("Please choose option 1 or 2")
def savingsChoice()
#if Savings account the user can choose Deposit or transfer
AccountChoice_input = None
    while AccountChoice_input != "1" or AccountChoice_input != "2":
        AccountChoice_input = input("Please choose (1)'Deposit' or (2)'Transfer': ")
        if AccountChoice_input == "1": 
            #deposit()
        elif AccountChoice_input == "2":
            #transfer()
        else:
            print("Please choose option 1 or 2")
def useService():
    #allow user to choose apply for loan or apply for credit card
    ServiceChoice_input = None
    while ServiceChoice_input != "1" or ServiceChoice_input != "2":
        ServiceChoice_input = input("Please choose (1)'Apply for Loan' or (2)'Apply for Credit Card': ")
        if ServiceChoice_input == "1": 
            #applyForLoan()
        elif AccountChoice_input == "2":
            #applyForCreditCard()
        else:
            print("Please choose option 1 or 2")
     
def applyForLoan()
    #approve loan if they have over 50,000 in savings account decline if under
            #if declined give them the option to set an employee meeting 
def applyForCreditCard()
    #approve credit card if they have credit score over 600 decline if under
            #if declined give them the option to set an employee meeting
startProgram()