compnum=50
count = 1
guess= int(input("Guess a number: "))
while guess!=compnum:
    if guess>compnum:
        print("Your guess is too high")
    else:
        print("Your guess is too low")
    count+=1    
    guess = int(input("Guess again: "))   
print(f"Well done, you took {count} attempts") 