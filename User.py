
class User():
    def __init__(self, name, password, contactInfo, authority):
        self.name = name
        self.password = password
        self.contactInfo = contactInfo
        self.authority = authority
        print("New User" + self.name)
    def getName(self):
        return self.name
    def getPassword(self):
        return self.password
    def getContactInfo(self):
        return self.contactInfo
    def getAuthority(self):
        return self.authority