n = 0
list = []
option = 0
while option != 9:
    print ("MENU")
    print ("--------------------------------------")
    print ("1.- Add a number to the list")
    print ("2.- Add a number in a position in the list")
    print ("3.- Show the length of the list")
    print ("4.- Delete the last number in the list")
    print ("5.- Delete a number in the list")
    print ("6.- Count numbers")
    print ("7.- Positions of a numbers")
    print ("8.- Show the list")
    print ("9.- Exit")

    option = int(input("Choose an option: "))
    
    if option == 1:

        n = int(input("Write a number to add at the list: "))
        list.append(n)
        print (list)

    elif option == 2:
        c = 0
        while(c == 0):

            n = int(input("Write a number to add at the list: "))
            position = int(input("Choose a position: "))

            if position > len(list):
                if len(list) == 0:
                    list.append(n)
                    break
                print ("The position doesn't exist")
                c = 0
            else:
                list.insert(position, n)
                c = 1
        print (list)
    
    elif option == 3:
        print("The length of the list is: ", len(list))

    elif option == 4:
        lenght = len(list)
        if len(list) > 0:
            list.pop(lenght-1)
            print(list)
        else:
            print("The list doesn't exist")

    elif option == 5:
        while(c == 0):

            n = int(input("what position do you want delete?: "))

            if n > len(list):
                print ("The position doesn't exist")
                c = 0
            else:
                list.pop(n)
                c = 1

    elif option == 6:
        n = int(input("Write a number: "))
        accountant = 0
        for x in list:
            if x == n:
                accountant = accountant + 1

        print("Your number appears", accountant, ("times in the list"))

    elif option == 7:
        n = int(input("Write a number: "))
        repeat = 0
        position = 0
        for x in list:
            position = position + 1
            if x == n:
                if repeat == 0:
                    print("Your number is in the position: ")
                    repeat = repeat + 1

                print(position)
        
        if repeat == 0:
            print("Your number doesn't exist in the list or the list hasn't been created")

    elif option == 8:
        print(list)
        
        

    
