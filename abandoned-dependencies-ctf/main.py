from password.password import *
from record.record import *
if __name__ ==  "__main__":
    name = input ("Full name: ")
    dob = input ("Date of birth: ")
    password = getpass("Passowrd: ")
    re_password = getpass("Verify your password: ")
    address = input("Address: ")
    phone = input("Phone number: ")
    
    # using function from "good" record package that simply creates a 
    # dictionary with all the above information
    record = createRecord(name, dob, password, address, phone)
    print("New record successfully created: \n")
    print(record)
