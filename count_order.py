order=input("DO you want to count from up or down(up/down): ")
if order=='up':
    number=int(input("Enter your top number to count from one to it as the last number: "))
    for i in range(1,number+1):
        print(i)
elif order=='down':
    num=int(input("Enter a number less than 20, to start counting down from 20 to that number: "))
    for j in range(20,num-1,-1):
        print(j)
else:
    print("I dont understand")