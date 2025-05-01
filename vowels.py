name=input("Enter your first name: ")
count=0
name.lower()
for x in name:
    if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
        count+=1
print(f"You have {count} vowels in {name}")