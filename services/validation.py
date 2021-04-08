import re
from controllers import employees_controller
# regex for email validation
regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

# Returns a message "Pass" when field is valid, custom message when invalid
def validate_field(type, field):
    if(type == "phone"):
        if(len(str(field)) > 10 or len(str(field)) < 10):
            return "Invalid phone number."
        else:
            return "Pass"
    elif(type == "email"):
        if(re.search(regex, field) == False):
            return "Invalid email."
        elif(employees_controller.email_is_taken(field)):
            return "That email is already taken. Please try another email."
        elif(re.search(regex, field)):
            return "Pass"
    elif(type == "first_name"):
        if(len(field) > 32):
            return "You exceeded the character limit for a first name. Please try abbreviating."
        elif (len(field) == 0):
            return "You must enter a first name."
        else:
            return "Pass"
    elif(type == "last_name"):
        if(len(field) > 32):
            return "You exceeded the character limit for a last name. Please try abbreviating."
        elif(len(field) == 0):
            return "You must enter a last name."
        else:
            return "Pass"
    elif(type == "title"):
        if(len(field) > 64):
            return "Title is too long. Please try to abbreviate."
        elif(len(field) == 0):
            return "You must enter a title."
        else:
            return "Pass"
    elif(type == "street"):
        if(len(field) > 120):
            return "Street address character limit exceeded."
        elif(len(field) == 0):
            return "You must enter a street address."
        else:
            return "Pass"
    elif(type == "city"):
        if(len(field) > 64):
            return "City character limit exceeded."
        elif(len(field) == 0):
            return "You must enter a city."
        else:
            return "Pass"
    elif(type == "state"):
        if(len(field) > 32 or len(field) == 0):
            return "You must enter a valid State."
        else:
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