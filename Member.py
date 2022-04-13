from User import *

class Member(User):
  def __init__(self, name, password, contactInfo, authority):
    super().__init__(name, password, contactInfo, authority)
    self.functions = ["Signout", "Schedule", "Balance"]