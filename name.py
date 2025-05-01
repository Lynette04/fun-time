#This is to merge the first name  and surname of a user and display the length of the full name.
firstname=input("Enter your first name: ")
print("The number of characters in your first name is : ",len(firstname))
surname=input("Enter your surname: ")
print("The number of characters in your surname is: ",len(surname))
name = firstname + " " + surname
print("Your full name is ",name)
print("The length of your full name is: ",len(name))