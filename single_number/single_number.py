'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # pop number from array and compare to remaining list
    # if number not in list save to variable and return
    num = 0
    current = arr[:]
    for i in arr:
        current.remove(i)
        if i not in current:
            num = i
        current = arr[:]
        i += 1
    return num


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")