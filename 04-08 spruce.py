def spruce(x):
	print("a spruce!")
	i = 1
	s = x - 1
	while i <= (x * 2):
	    print((" " * s) + ("*" * i))
	    i += 2
	    s -= 1
	print((" " * (x-1)) + ("*"))




# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)

### potential solution
#def spruce(number):
    #print("a spruce!")
    #i = 1
    #while i <= number:
        #print(" " * (number -i) + "*" * (2 * i - 1))
        #i += 1
    #print(" " * (number - 1) + "*")

#spruce(6)


#the separator in print by default it will add a space between the parameters
#print("a", "b")
#>>>a b

#print("a", "b", sep="")
#>>>ab

#print("a", "b", sep="??")
#>>>a??b