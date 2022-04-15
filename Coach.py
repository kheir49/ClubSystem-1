from User import *

class Coach(User):
  #Class Init
  def __init__(self, name, password, contactInfo, authority):
    #Inherit
    super().__init__(name, password, contactInfo, authority)
    #Useable Functions
    self.functions = ["Balance", "Create Announcement", "Message Student","Pay", "Members"]
  def findClass(date):
  def classAnnouncement(batch, message):
    batch.append(message)
  def messageStudent(batch, name, message):
    for student in batch.get_batch():
      if(name == student.name.lower()):
        student.messagesReceived.append(message)
  def getFunction(self):
    return self.functions
  def useFunction(self, userInput):
    #Balance
    if(userInput.lower() == functions[0].lower()):
      print(self.balance)
    #Hire
    elif(userInput.lower() == functions[1].lower()):
      self.classAnnouncements()
    #Message
    elif(userInput.lower() == functions[2].lower()):
      userInput1 = input("Please Enter the Batch: ")
      userInput2 = input("Please Enter the Students Name: ")
      userInput3 = input("Please enter your message: ")
      self.messageStudent(userInput1, userInput2, userInput3)
    #Pay
    elif(userInput.lower() == functions[3].lower()):
      self.Pay()
    #Members List
    elif(userInput.lower() == functions[4].lower()):
      self.Members()
    #Invalid
    else
      print("Invalid user input")