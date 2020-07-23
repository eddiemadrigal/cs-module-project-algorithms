'''
For example, given [1, 7, 3, 4]
your function should return: [84,    12,    28,    21   ]
by calculating:              [7*3*4, 1*3*4, 1*7*4, 1*7*3]
'''
def product_of_all_other_numbers(arr):          # function definition
    finalProduct = 1                            # finalProduct variable initialized to 1
    finalArr = []                               # finalArr array initialized

    for el in arr:                              # for each element in the received array
        finalProduct *= el                      # finalProduct is the finalProduct multiplied by the value of the element

    for eaEl in arr:                            # for each element in the received array
        finalArr.append(finalProduct // eaEl)   # append to the finalArr the total multiplied product divided by the value of the current element

    return finalArr                             # return the final array


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]
    # arr = [1, 7, 3, 4]
    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
