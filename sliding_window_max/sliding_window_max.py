'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers

Sample Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Expected Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
-------------------------     -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

'''
def sliding_window_max(nums, k):            # function defined
    i = len(nums)                           # find the number of iterations (i)
    end = i - k + 1                         # iterations - window size + the first window => end
    windowArr = []                          # array found in the window
    maxValues = []                          # max value found in each window
    start = 0                               # start variable initialized to zero
    for i in range(0, end):                 # for every element in the range, starting at zero to end
        for j in range(start, k + start):   # for every group of elements
            windowArr.append(nums[j])       # append the elements found in that window size
        maxValues.append(max(windowArr))    # append the max value found in the window array
        start += 1                          # move the starting value to the right
    return maxValues                        # return the array of max values per grouping

# k = 5: 
if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7, 9, 11, 2]
    k = 7

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

    # [3, 3, 5, 5, 6, 7]