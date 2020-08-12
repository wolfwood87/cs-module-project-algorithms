'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    #recursively call eating cookies down to 1
    #add to n

    if n <= 1:
        return 1
    else:
        print(n)
        if n % 2 == 0:
            return n + eating_cookies(n-1)
        else:
            return n + eating_cookies(n-1)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
