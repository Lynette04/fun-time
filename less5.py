#The program asks the user to enter a number less than or equal to 5.
#if not, the program alerts the user that their input is above 5.
num=0
while num<=5:
    num=int(input("Enter a number less or equal to 5: "))
print(f"Oops! The last number you entered was a {num} which is greater than 5.")