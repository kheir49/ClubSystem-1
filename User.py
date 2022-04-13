
class User():
    functions = []
    def __init__(self, name, password, contactInfo, authority):
        self.name = name
        self.password = password
        self.contactInfo = contactInfo
        self.authority = authority

    def getName(self):
        return self.name
    def getPassword(self):
        return self.password
    def getContactInfo(self):
        return self.contactInfo
    def getAuthority(self):
        return self.authority
    def userLogin(self):
        while True:
            print(self.functions)
            userInput = input("What would you like to do?: ")
            if(userInput == "Signout"):
                break