from User import *
from Treasurer import *
from Coach import *
Users = [] # For storing the Users instances
def main():
    Users.append(Treasurer("Tom", "abc123", "5102775199", "Treasurer"))
    print("Welcome to the Club Digital System")
    print("If you are a returning Users, enter your Username and password,\nOtherwise Type 'Create'")
    username = input("Please Enter Your Username: ")
    if(username == "Create"):
        name = input("Please Enter Your Name: ")
        contactInfo = input("Please Enter Your Contact Information, This will be used as your Account's Username: ")
        password = input("Please Enter Your Password: ")
        authority = input("Please Enter Your Account Type(Ex: Member, Coach, or Treasurer): ")
        Users.append(Users(name, password, contactInfo, authority))
    else:
        password = input("Please Enter Your Password: ")
    for i in range(len(Users)):
        if(Users[i].contactInfo == username and Users[i].password == password):
            name = Users[i].name
            authority = Users[i].authority
            print("Welcome " + name)
            Users[0].userLogin()
if __name__ == "__main__":
    main()