#To check if a word is in upper case
word=input("Type a word in upper case: ")
again= False
while again==False:
    if word.isupper():
        print("Well done!")
        break
    else:
        print("Try again")
        word=input("Type a word in upper case: ")