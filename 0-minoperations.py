def minOperations(n):
    if n <= 0:
        return 0

    # Initialize an array to store the minimum number of operations for each number of characters
    dp = [float('inf')] * (n + 1)

    # Base case: 1 operation to get 1 character
    dp[1] = 0

    # Iterate from 2 to n
    for i in range(2, n + 1):
        # Try all possible factors of i
        for j in range(1, i):
            if i % j == 0:
                # Calculate the number of operations needed for each factor and update dp[i]
                dp[i] = min(dp[i], dp[j] + i // j)

    # If dp[n] is still infinity, it means n is impossible to achieve
    return dp[n] if dp[n] != float('inf') else 0

# Testing the example cases
n1 = 4
print("Min # of operations to reach {} char: {}".format(n1, minOperations(n1)))

n2 = 12
print("Min # of operations to reach {} char: {}".format(n2, minOperations(n2)))

