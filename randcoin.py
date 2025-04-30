#This program asks the user to choose between heads and tails.
#A side is chosen at random by the computer. The aim is to see if the side and the choice correspond.
import random
side = random.choice(["h","t"])
choice= input("Choose between heads(h) or tails(t): ")
if choice==side:
    print("You win!")
else:
    print("Bad luck")
print(f"The computer chose {side}.")    