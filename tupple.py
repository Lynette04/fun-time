#This demonstrates a simple tuple and some operations involved
countries_tuple=("Uganda","Kenya","Burundi","Rwanda","Tanzania")
print(countries_tuple)
answer=input("Name any one of the countries shown: ")
print(countries_tuple.index(answer))
number=int(input("Enter a number to display a country from the list shown: "))
print(countries_tuple[number])
