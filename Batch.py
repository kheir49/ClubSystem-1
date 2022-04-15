
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
    
    def enroll(self, Member): #enrolls member to the Batch, adds member object to the students list
        self.students.append(Member)

    def sort_batch_attendence(self): #sorts batch by the the number of attendence
        dicts = {}
        
        for i in range(len(self.students)):
            dicts[self.students[i].name] = self.students[i].attended

        sorted(dicts.items(), key=lambda x: x[1], reverse=True)

        self.memberA = list(dicts.keys())  

        return self.memberA      

    def sort_batch_paid(self): #sorts batch by the amount of times they paid or not
        pass