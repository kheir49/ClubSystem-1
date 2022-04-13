from User import *

class Member(User):
    def __init__(self, name, password, contactInfo, authority):
        super().__init__(name, password, contactInfo, authority)
        self.functions = ["Signout", "Schedule", "Balance"]
        self.balance = 0
        self.attendence = 0
        self.totalClasses = 0
        self.paymentDue = False
        self.willAttend = False
        self.discount = False
        self.penalteeFee = False
        self.termination = False
    def Pay(Amount):
    def Schedule(date):