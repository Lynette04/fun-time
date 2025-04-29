#This is a program that asks the user to enter a number between 10 and 20.
#if the number is less than 10 or greater than 20, the user is prompted to try again.
num = int(input("Enter a number between 10 and 20: "))
while num<10 or num>20:
    if num<10:
        print("Too low")
    else:
        print("Too high")
    num = int(input("Enter a number between 10 and 20: "))
print("Thank you")        