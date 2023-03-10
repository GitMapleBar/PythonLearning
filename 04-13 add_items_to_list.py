length = int(input("How many items: "))
i = 1
list = []
while i <= length:
    item = int(input(f"Item {i}: "))
    i += 1
    list.append(item)
print(list)