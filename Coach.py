from User import *

class Coach(User):
  def __init__(self, name, password, contactInfo, authority):
    super().__init__(name, password, contactInfo, authority)
    self.functions = ["Signout", "Hire", "Pay", "Balance", "Members"]
  def findClass(date):
  def classAnnouncement(batch, message):
  def classAnnouncement(batch, name, message):