my_list = [1, 2, 3, 4, 5]
index = 0
while True:
    index = int(input("Index: "))
    if index == -1:
        break
    newval = int(input("New value: "))
    my_list[index] = newval
    print(my_list)

    