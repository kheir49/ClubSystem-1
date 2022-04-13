
class Batch():
    def __init__(self, name, instructor, sizeCap):
        self.name = name
        self.instructor = instructor
        self.sizeCap = sizeCap
        self.currentSize = 0