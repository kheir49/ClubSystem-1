from User import *

class Member(User):
    #Class Init
    def __init__(self, name, password, contactInfo, authority):
        #Inherit
        super().__init__(name, password, contactInfo, authority)
        #Useable Functions
        self.functions = ["Signout", "Balance", "Schedule"]
        self.balance = 0
        self.attended = 0
        self.totalClasses = 0
        self.paymentDue = False
        self.willAttend = False
        self.discount = False
        self.penalteeFee = False
        self.termination = False
    def Pay(self, Amount):
        #Subtract amount from self
        self.balance -= Amount
        #Return Amount being paid to its destination
        return Amount
    def Schedule(self):
        userInput = input("What would you like to do?: ")
    def getFunction(self):
        return self.functions
    def useFunction(self, userInput):
            #Balance
            if(userInput.lower() == functions[1].lower()):
                print(self.balance)
            #Schedule
            elif(userInput.lower() == functions[2].lower()):
                self.Schedule()
            #Invalid Input
            else:
                print("Invalid user input")