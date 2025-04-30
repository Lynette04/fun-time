#This is a simple calculator to carry out the basic math operations on 2 integers.
num1= int(input("Enter a number: "))
num2=int(input("Enter another number: "))

operation= input("Enter an operation of your choice('+','-','*','/'): ")

if operation=='+':
    print("the sum is ",num1+num2)
elif operation=='-':
    print("The difference is ",num1-num2)
elif operation=='*':
    print("The product is: ",num1*num2)
elif operation=='/':
    print("The quotient is ",num1/num2)
else:
    print("that is not a valid operation")