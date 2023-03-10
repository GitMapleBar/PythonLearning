list = []
while True:
    word = str.lower(input("Word: "))
    if word in list:
        print("You typed in", len(list),"different words")
        break
    else:
        list.append(word)