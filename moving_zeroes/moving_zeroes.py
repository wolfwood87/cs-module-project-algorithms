'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # loop through the array and remove and append at the end if zero
    i = 0
    while i < len(arr):
        if arr[i] != 0:
            temp = arr.pop(i)
            print(arr)
            arr.insert(0, temp)
            print(arr)
            i += 1
        else:
            i += 1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")