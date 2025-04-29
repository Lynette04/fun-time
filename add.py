#This program asks the user to input 2 integers. The 2 integers are added together and the user is asked if they want to add aanother integer.
#If yes, they input another integer and keep adding more integers until they dont want to. then the total is displayed.

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
sum = num1 + num2
question=input("Do you want to add another number(y/n): ")
while question=='y':
    number=int(input("Enter a number to add: "))
    sum+=number
    question=input("Do you want to add another number(y/n): ")
print(f"The total is {sum}")    
