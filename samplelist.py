#this demonstrates some operations that can be carried out on a list
sports_list=["Basketball","Soccer","Tennis","Swimming","Baseball","javelin","Hockey"]
answer=input("What is sport can i add to this list?: ")
sports_list.append(answer)
sports_list.sort()
print(sports_list)
answer2=input("Which sport should i remove: ")
sports_list.remove(answer2)
print(sports_list)
start= int(input("Give me a number between 0 and 3:  "))
end= int(input("Give me a number between 4 and 7: "))
print(sports_list[start:end],f"are the sports from {start} to {end}. ")