'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    myNums = []
    ans = arr[0]
    for i in range(1, len(arr)):
        ans ^= arr[i] # bitwise xor and assigns the value to ans. if xor is the same, 0 is returned        
    return ans

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")