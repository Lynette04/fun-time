#This simple program asks the user to enter 5 numbers 
# and after each input the program asks the user if they want to add the input numbers to make the total. 
# Initially the total has been set to 0 and then it will be cumulative depending on the response of the user.
total=0
for i in range(0,5):
   num=int(input("Enter a number: "))
   que1=input("Do you want to add this number to the total?(yes/no): ")
   if que1=='yes':
       total+=num
print(f"total={total}")