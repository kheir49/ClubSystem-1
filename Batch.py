
from Member import * 

class Batch():
    def __init__(self, name, date, instructor, sizeCap):
        self.name = name
        self.date = date
        self.instructor = instructor
        self.sizeCap = sizeCap
        self.currentSize = 0
        self.students = []
        self.membersA = []
        self.membersP = []
        self.announcements = []
        self.functions = ["Enroll","Sort by attendence","Sort by fee paid"]


    def get_batch(self):
        return self.students #returns a list of members currently enrolled in the batch
    
    def enroll(): #enrolls member to the Batch
        pass

    def sort_batch_attendence(self): #sorts batch by the the number of attendence
        pass

    def sort_batch_paid(self): #sorts batch by the amount of times they paid or not
        pass