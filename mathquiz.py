#This is a math quiz where 2 integers selected at random by the computer are summed up.
#the user is asked to guess a sum five times and their score is generated out of 5 for each correct answer.
import random
score=0
for i in range(1,6):
  num1=random.randint(1,10)
  num2=random.randint(1,10)
  sum= num1 + num2
  answer=int(input("What is your answer from a sum of 2 random numbers between 1 aand 10 inclusive:  "))
  if answer==sum:
      print("You are correct")
      score+=1
  else:
      print("Wrong")    
print(f"You scored {score} out of 5")

