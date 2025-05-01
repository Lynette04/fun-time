#To display passwords and check if they are exactly the same
password1=input("Enter a password: ")
password2=input("Enter it again: ")
if password1==password2:
    print("Correct")
elif password1.lower()==password2.lower():
    print("They must be in the same case")
else:
    print("Incorrect")