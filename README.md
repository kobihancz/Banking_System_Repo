# **Banking_System_Project**

##Introduction
This is a project inspired by Springboards Data Engineering Track. It is a simple Banking system that encorporates UI with object oriented programming, while refrencing and drawing data from json files.

##File Structure
*Classes \- Includes the 4 classes required in project instructions
  *Account.py \- An account takes in a customer ID and a balance and can perom a deposit, write account to db, and update customer info on an instantiated account      object. To instatntiate an object pass in a balance and customer id from either user input or a refrence to the Database system 
    *Checking \- A checking is a child class of the Accounts class and takes in a customer ID and a balance and can perom a withrawl on an instantiated checking          object. To instatntiate an object pass in a balance and customer id from either user input or a refrence to the Database system.
    *Saving \- A Saving is a child class of the Accounts class and takes in a customer ID and a balance and can perom a withrawl on an instantiated saving                object. To instatntiate an object pass in a balance and customer id from either user input or a refrence to the Database system.
   *Customer.py \- A customer takes in a customerID, name , ssn, address, age, creditScore and can write customer to db. To instantiate a object pass in a              customerID, name , ssn, address, age, creditScore from either user input or a refrence to the Database system.
   *Employee.py \- An Employee takes in employee_id, name, department. It's sole purpose is to instantiate an employee object. 
   *Service.py \- A service takes in a customer_ID, name, savingsBalance, creditScore, department and can perom a generate random request ID, write request to db,      write service to history, approve or decline loan, approve or decline creditCard on an instantiated service object. To instatntiate an object pass in a              customer_ID, name, savingsBalance, creditScore, department from either user input or a refrence to the Database system 
 *Database \- 4 Data files using the .Json format and one text file to record history
   *Accounts.json
   *Customers.json
   *Employees.json
   *PendingReqests.json
   *ServiceHistory.txt
 *Logs \- 2 txt files that log all the errors and warnings from customer info input
   *Errors.txt
   *warnings.txt
 *Test \- test file that records tests to fix problems
 *Utilities \- Contains the Log file which applies functionality to Warnings and Errors
    *Log.py \- Performs 3 methods warning, error, write to file. This functionality is used in the banking system to check the user inputs when creating a new            customer.
 *BankingSystem.py \- This is the Banking system that takes in user input and allows the user to perform all the functions of the banking system. 
 \-It starts by allowing the User to choose Customer or Employee.
 \-If the user chooses employee they can log in as an employee in the Loan or CreditCard department.They then can see all the pending requests for their department    and approve or deny each one.
 \-If the user chooses Customer they can then choose to LogIn or SignUp
 \-If the user chooses LogIn they input an existing Customer Id and Choose an activity
 \-If the user chooses SignUp they input a customerID, name , ssn, address, age, creditScore and choose an activity
 \-The user can then choose accountSummary or useService.
 \-If the user chooses useService they can either apply for Loan for apply for Credit Card
 \-If the user chooser accountSummary it will display the accounts associated with that CustomerID. they can then choose to interact with the checking account or      interact with the savings account.
 \-If the user chooses Savingschoice they can either make a deposit or withdrawl and if the choose checkings choice they can either choose deposit or transfer. 
 
    
  

 
