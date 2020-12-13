
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
            logIn()
            chooseActivity()
        elif CustomerChoice_input == "2":
            signUp()
            chooseActivity()
        else:
            print("Please choose option 1 or 2")
#employee logs in using their employee ID
def employeeChoice():
    log_inEmployeeid_input = input("Employee ID: ")
    #in this function make sure the input is valid 

def logIn():
    log_inCustomerid_input = input("Customer ID: ")
    #in this function make sure the input is valid

def signUp():
    Customerid_input = input("Customer ID: ") 
    name_input = input("Name: ")
    ssn_input = input("Social Security #: ")
    #accounts_input = input("Choose to open checking and savings or just checking: ")
    address_input = input("Address: ")
    age_input = input("Age: ")
    creditScore_input = input("Credit Score: ")
    #create customer in db
    #create accounts in db 
    #check all inputs

def chooseActivity():
    ActivityChoice_input = None
    while ActivityChoice_input != "1" or ActivityChoice_input != "2":
        CustomerChoice_input = input("Please choose (1)'Accounts Summary' or (2)'Use Service': ")
        if CustomerChoice_input == "1":
            pass
            #accountsSummary()
        elif CustomerChoice_input == "2":
            pass
            #useService()
        else:
            print("Please choose option 1 or 2") 

#def accountsSummary():
startProgram()