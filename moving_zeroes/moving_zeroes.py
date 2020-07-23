'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    count = 0                               # count of non-zero elements
    remainingZeroCount = 0                  # count of zero elements
    updateArr = []                          # updated array of non-zero elements   
    for el in range(len(arr)):              # iterate through 
        if arr[el] != 0:                    # check each el if it's not a zero
            count += 1                      # update non-zero count
            updateArr.append(arr[el])       # append non-zero element
        elif arr[el] == 0:                  # if a zero is found
            remainingZeroCount += 1         # increase zero count
    zeroCount = 0                           # initialize zero count to 0
    while zeroCount < remainingZeroCount:   # while loop runs zeroCount times
        updateArr.append(0)                 # for every zeroCount, append a zero
        zeroCount += 1                      # increment the zeroCount by 1
        
    return updateArr                        # return the updated array



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")