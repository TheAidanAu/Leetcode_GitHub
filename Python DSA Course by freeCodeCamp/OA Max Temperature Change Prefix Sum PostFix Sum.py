# Find the maximum aggregate temperature changed evaluated among all the days.
# ex - [-1,2,3] - 5
# explanation -
# [-1],[-1,2,3] - max(-1,4) = 4
# [-1,2],[2,3] - max(1,5) = 5
# [-1,2,3][3] - max(4,3) = 4

def max_aggregate_temperature_change(arr):
    n = len(arr)

    # Calculate Prefix Sum Array
    prefix_sum = [0] * n
    prefix_sum[0] = arr[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]

    # Calculate Postfix Sum Array
    postfix_sum = [0] * n
    postfix_sum[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        postfix_sum[i] = postfix_sum[i + 1] + arr[i]

    max_temperature_change = float('-inf')
    for i in range(n):
        max_temperature_change = max(max_temperature_change, max(prefix_sum[i], postfix_sum[i]))

    return max_temperature_change


# Test the function
arr = [-1, 2, 3]
result = max_aggregate_temperature_change(arr)
print(result)  # Output: 5
