#This program demonstrates the song "10 green bottles"
num = 10
while num!=0:
    print(f"There are {num} green bottles hanging on the wall.")
    print(f"{num} green bottles hanging on the wall") 
    print("and if 1 green bottle should accidentally fall")
    question= int(input("How many green bottles will be hanging on the wall?: "))
    if question==num-1:
        print(f"There will be {num-1} green bottles hanging on the wall. ")
        num-=1 
    else:
        print("No try again")
     
print("There are no more green bottles hangiing on the wall.")      