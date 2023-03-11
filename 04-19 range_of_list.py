def range_of_list(list):
    return max(list) - min(list)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    result = range_of_list([3, 6, -4])
    print(f"The range of the list is {result}")