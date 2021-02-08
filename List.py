lis = ["1", "hello", "blue", "bangalore"]
choice = ''
while(True):
    
    print(f'''                L I S T      M A N I P U L A T I O N                  
    1.Append an element
    2.Insert an element at a desired position
    3.Append a list to the given list
    4.Modify an existing element
    5.Delete an existing element by it's position
    6.Delete an existing element by it's value
    7.Sort the list in ascending order 
    8.Sort the list in descending order
    9.Exit
    The list has the following elements: {lis}
    ''')
    choice = input("Enter you choice (1-9): ")
    if choice == '1':
        element = (input("Enter the element to be appended: "))
        lis.append(element)
        print("The element has been appended\n")
        
    elif choice == '2':
        element = (input("Enter the element to be inserted: "))
        position = int(input("Enter the position:"))
        lis.insert(position,element)
        print("The element has been inserted\n")
    
    elif choice == '3':
        newList = input("Enter the list to be appended(Do not use quotes, and use (,) for separating the elements): ")
        lis.extend(list(newList.split(",")))
        print("The list has been appended\n")
    
    elif choice == '4':
        i = int(input("Enter the position of the element to be modified: "))
        
        if i < len(lis):
            
            newElement = (input("Enter the new element: "))
            oldElement = lis[i]
            lis[i] = newElement
            print("The element",oldElement,"has been modified\n")
        else:
            print("Position of the element is more than the length of list")
    
    elif choice == '5':
        i = int((input("Enter the position of the element to be deleted: ")))
        if i < len(lis):
            element = lis.pop(i)
            print("The element",element,"has been deleted\n")
        else:
            print("\nPosition of the element is more than the length of list")
    
    elif choice == '6':
        element = (input("\nEnter the element to be deleted: "))
        if element in lis:
            lis.remove(element)
            print("\nThe element",element,"has been deleted\n")
        else:
            print("\nElement",element,"is not present in the list")
    

    

    elif choice == '7':
        lis.sort()
        print("\nThe list has been sorted")
    
    elif choice == '8':
        lis.sort(reverse = True)
        print("\nThe list has been sorted in reverse order")
    
    
    elif choice == '9':
        break
    else:
        print("Choice is not valid")
        print("\n\nPress any key to continue")
        ch = input()
