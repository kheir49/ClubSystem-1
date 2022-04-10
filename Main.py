

def main():
    print("Welcome to the Club Digital System")
    print("If you are a returning user, enter your username and password,\nOtherwise Type 'Create'")
    username = input("Please Enter Your Username: ")
    if(username == "Create"):
        name = input("Please Enter Your Name: ")
        contactInfo = input("Please Enter Your Contact Information, This will be used as your Account's Username: ")
        password = input("Please Enter Your Password: ")
        authority = input("Please Enter Your Account Type(Ex: Member, Coach, or Treasurer): ")
    else:
        password = input("Please Enter Your Password")
        

if __name__ == "__main__":
    main()