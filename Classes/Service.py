import json

class Service:
    
    def __init__(self, customer_ID, name, savingsBalance, creditScore, department):
        self.request_ID = self.generate_random_request_ID()
        self.customer_ID = customer_ID
        self.name = name 
        self.savingsBalance = savingsBalance
        self.creditScore = creditScore
        self.department = department

    def generate_random_request_ID(self):
        with open("/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Database/PendingRequests.json", 'r') as requestf:
            file_dict = json.load(requestf)
            request_id = file_dict["request_id_counter"]
            file_dict["request_id_counter"] += 1
        with open("/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Database/PendingRequests.json", 'w') as requestf:
            json.dump(file_dict,requestf)
        return request_id

    def write_request_to_db(self):
        with open("/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Database/PendingRequests.json", 'r') as requestf:
            file_dict = json.load(requestf)
            file_dict["Requests"].append(self.__dict__)
        with open("/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Database/PendingRequests.json", 'w') as requestf:
            json.dump(file_dict,requestf)

    def write_service_to_history(self):
        with open("/Users/kobihancz/Desktop/Banking_System_Project/Banking_System_Repo/Database/ServiceHistory.txt", 'a') as historyf:
            historyf.write(f'Request {self.request_ID} has been approved'+'\n')
    
    def approve_or_decline_loan(self):
        if self.savingsBalance >= 50000:
            return True
        else:
            return False

    def approve_or_decline_creditCard(self):
        if self.creditScore  >= 600:
            return True
        else:
            return False

