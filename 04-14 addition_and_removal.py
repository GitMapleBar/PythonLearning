list = []
number = 0
while True:
    print(f"The list is now {list}")
    option = str.lower(input("a(d)d, (r)emove or e(x)it: "))
    if option == "x":
        print("Bye!")
        break
    elif option == "d":
        number += 1
        list.append(number)
    elif option == "r":
        list.remove(number)
        number -= 1
######### Solution
#list = []
#while True:
    #print(f"The list is now {list}")
    #selection = input("a(d)d, (r)emove or e(x)it:")
    #if selection == "d":
        # Value of item is length of the list + 1
        #item = len(list) + 1
        #list.append(item)
    #elif selection == "r":
        #list.pop(len(list) - 1)
    #elif selection == "x":
        #break
 
#print("Bye!")