#this is a program to display the name of a person who has been invited to a party
#the user is asked for a number below 10 to invite, if the number is above 10, the program displays "too many people".
people = int(input("How many people do you want to invite to your party?: "))
if people<10:
    for j in range(0,people):
       name= input("What is the name of the person?: ")
       print(f"{name} has been invited")
else:
    print("Too many people")        