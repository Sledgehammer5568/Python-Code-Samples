# Emanuel Ramos
#
# 10/19/2022
#
# Description: this program prints out a greeting only for emanuel and ronan
#

# Any name can be inputted but only certain names will receive a greeting.
user = input("What is your name?\n")

# If "emanuel" is inputted they will receive a greeting.
if user == "emanuel":
    print("Hello! Good day to you! " + user + ".")

# If "ronan" is inputted they will also receive a greeting.
elif user == "ronan":
    print("Hello! Good day to you! " + user + ".")

# If anything else is inputted they will not get a greeting.
else:
    print("You are not allowed!!!")
