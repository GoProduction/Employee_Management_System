import re
from controllers import employees_controller
# regex for email validation
regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

# Returns a message "Pass" when field is valid, custom message when invalid
def validate_field(id, type, field):
    if(type == "phone"):
        print('Checking phone')
        if(len(str(field)) > 10 or len(str(field)) < 10):
            print('Phone: Invalid')
            return "Invalid phone number."
        else:
            print('Phone: Pass')
            return "Pass"
    elif(type == "email"):
        print("Checking email")
        if(len(field) == 0):
            print("Email: Empty")
            return "You must enter an email"
        elif(re.search(regex, field) == False):
            print("Email: Invalid")
            return "Invalid email."
        elif(employees_controller.email_is_taken(id, field)):
            print("Email: Taken")
            return "That email is already taken. Please try another email."
        else:
            return "Pass"
    elif(type == "first_name"):
        print("Checking first name")
        if(len(field) > 32):
            print("First name: Too long")
            return "You exceeded the character limit for a first name. Please try abbreviating."
        elif (len(field) == 0):
            print("First name: Empty")
            return "You must enter a first name."
        else:
            print("First name: Pass")
            return "Pass"
    elif(type == "last_name"):
        print("Checking last name")
        if(len(field) > 32):
            print("Last name: Too long")
            return "You exceeded the character limit for a last name. Please try abbreviating."
        elif(len(field) == 0):
            print("Last name: Empty")
            return "You must enter a last name."
        else:
            print("Last name: Pass")
            return "Pass"
    elif(type == "title"):
        print("Checking title")
        if(len(field) > 64):
            print("Title: Too long")
            return "Title is too long. Please try to abbreviate."
        elif(len(field) == 0):
            print("Title: Empty")
            return "You must enter a title."
        else:
            print("Title: Pass")
            return "Pass"
    elif(type == "address"):
        print("Checking street")
        if(len(field) > 120):
            print("Street: Too long")
            return "Street address character limit exceeded."
        elif(len(field) == 0):
            print("Street: empty")
            return "You must enter a street address."
        else:
            print("Street: Pass")
            return "Pass"
    elif(type == "city"):
        print("Checking city")
        if(len(field) > 64):
            print("City: Too long")
            return "City character limit exceeded."
        elif(len(field) == 0):
            print("City: Empty")
            return "You must enter a city."
        else:
            print("City: Pass")
            return "Pass"
    elif(type == "state"):
        print("Checking state")
        if(field == -1):
            print("State: Not selected")
            return "You must enter a valid State."
        else:
            print("State: Pass")
            return "Pass"
    elif(type == "zip"):
        if(len(str(field)) > 38):
            return "Zip code is too long."
        elif(len(str(field)) == 0):
            return "You must enter a zip code."
        else:
            return "Pass"
    elif(type == "license"):
        if(len(field) > 24):
            return "License character limit exceeded."
        elif(len(field) == 0):
            return "You must enter a license/ID number."
        else:
            return "Pass"
    elif(type == "ssn"):
        if(len(str(field)) > 9 or len(str(field)) < 9):
            return "Invalid Social Security Number"
        else:
            return "Pass"
    elif(type == "department"):
        if(field == -1):
            return "You must select a valid department"
        else:
            return "Pass"