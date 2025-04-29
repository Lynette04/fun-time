#This program counts the number of people invited to a party using a while loop
count = 0
question=input("Do you want to invite someone (y/n): ")
while question=='y':
    name = input("Enter the name of a person to invite: ")
    print(f"{name} has now been invited.")
    count+=1
    question=input("Do you want to invite someone else (y/n): ")
print(f"You have invited {count} people to your party")    