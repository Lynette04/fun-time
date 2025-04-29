#This programs starts with the total as 0 and asks the user to input numbers. 
#Once the total is above 50, the loop will stop. It is implementing a while loop.
total=0
while total<=50:
    num=int(input("Enter a number less than 50: "))
    total= total+num
    print(f"The total is {total}")   