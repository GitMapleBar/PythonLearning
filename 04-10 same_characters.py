def same_chars(string, x, y):
    if x > len(string) - 1 or y > len(string) - 1:
        return False
    a = string[x]
    b = string[y]
    if a == b:
        return True
    elif a != y:
        return False
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 10))

##model
#def same_chars(str, a, b):
    #if a >= len(str) or b >= len(str):
        #return False
    #return str[a] == str[b] << Smart. uses Boolean, if a == b, True.
#print(same_chars("codoa", 2, 2))