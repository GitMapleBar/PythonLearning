def greatest_number(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    elif z >= x and z >= y:
        return z
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(3, 1, 4)
    print(greatest)

##model
#def greatest_number(a, b, c):
    #if a >= b and a >= c:
        #return a
    #elif b >= c:  here, we know a is not >=b since we are now at the next elif statement, so we jsut need b>= c since we know a is < b
        #return b
    #else:
        #return c