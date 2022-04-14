from User import *

class Coach(User):
  #Class Init
  def __init__(self, name, password, contactInfo, authority):
    #Inherit
    super().__init__(name, password, contactInfo, authority)
    #Useable Functions
    self.functions = ["Signout", "Balance", "Hire", "Pay", "Members"]
  def findClass(date):
  def classAnnouncement(batch, message):
  def messageStudent(batch, name, message):
  def getFunction(self):
    return self.functions
  def useFunction(self, userInput):
    #Balance
    if(userInput.lower() == functions[1].lower()):
      print(self.balance)
    #Hire
    elif(userInput.lower() == functions[2].lower()):
      self.Hire()
    #Pay
    elif(userInput.lower() == functions[3].lower()):
      self.Pay()
    #Members List
    elif(userInput.lower() == functions[4].lower()):
      self.Members()
    #Invalid
    else
      print("Invalid user input")