array=[2,3,4,6,7,8,9,5,1]
#to add an element to the existing array
def add_element():
    element= int(input("Enter a number to add to the array: "))
    array.append(element)
#to display the current array
def display_current_array():
    print("Current array: ",array)
#to remove an element from the array using its index
def remove_by_index():
    index = int(input("Enter index to remove: "))
    if index>=0 and index<len(array):
            array.pop(index)
    else:
        print("Invalid index")
#to display the length or size of the array
def display_length():
    print("The length of the array is : ",len(array))  
#to remove everything from the array
def clear_array():
    array.clear()          
#to check if an element exists in an array
def check_existence():
    element= int(input("Enter number to check if in array: "))
    if element in array:
        print(f"The element {element} is in the array")
    else:
        print(f"the element {element} doesnt exist in the array.")
#to sort the array in either ascending or descending order.
def sort_array():
    order = input("Enter the order to sort (asc/desc): ")
    if order == "asc":
        array.sort()
    elif order== "desc":
        array.sort(reverse=True) 
    else:
        print("Invalid order")
       
#calling the functions       
add_element() 
display_current_array()
remove_by_index()  
display_current_array()
display_length() 
check_existence()
sort_array()
display_current_array()
clear_array()
display_current_array()