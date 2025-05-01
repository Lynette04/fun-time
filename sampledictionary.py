#This is a simple implementation of a dictionary
food_dictionary={}
food1=input("What is your most favorite food: ")
food_dictionary[1]=food1
food2=input("What is your second favorite food: ")
food_dictionary[2]=food2
food3=input("What is your third favorite food: ")
food_dictionary[3]=food3
food4=input("What is your fourth favorite food: ")
food_dictionary[4]=food4
print(food_dictionary)

removed_food=int(input("What food do you want to delete from the list(1,2,3 or 4): "))
del food_dictionary[removed_food]
print(food_dictionary)
print(sorted(food_dictionary.values()))
food_dictionary[5]=input("Add a fruit: ")
print(food_dictionary)