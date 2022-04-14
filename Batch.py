
class Batch():
    def __init__(self, name, date, instructor, sizeCap):
        self.name = name
        self.date = date
        self.instructor = instructor
        self.sizeCap = sizeCap
        self.currentSize = 0
        self.students = []