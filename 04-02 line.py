# Write your solution here
def line (x, string):
    if string == "":
        string = "*"
    print(string[0] * x)



# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(6, "")