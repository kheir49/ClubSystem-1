from User import *
class Treasurer(User):
    def __init__(self, name, password, contactInfo, authority):
        super().__init__(name, password, contactInfo, authority)
    