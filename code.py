def find_maximum_sum(grid):
    rows = len(grid)
    cols = len(grid[0])

    # Create a 2D array to store the maximum sum values
    dp = [[0] * cols for _ in range(rows)]

    # Initialize the first cell with the starting value
    dp[0][0] = 0 if grid[0][0] == 'S' else int(grid[0][0])

    # Initialize the first row
    for j in range(1, cols):
        if grid[0][j] == 'S':
            dp[0][j] = dp[0][j-1]
        elif grid[0][j] != 'F':
            dp[0][j] = dp[0][j-1] + int(grid[0][j])
        else:
            dp[0][j] = dp[0][j-1]

    # Initialize the first column
    for i in range(1, rows):
        if grid[i][0] == 'S':
            dp[i][0] = dp[i-1][0]
        elif grid[i][0] != 'F':
            dp[i][0] = dp[i-1][0] + int(grid[i][0])
        else:
            dp[i][0] = dp[i-1][0]

    # Fill the dp array using the recurrence relation
    for i in range(1, rows):
        for j in range(1, cols):
            if grid[i][j] == 'S':
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            elif grid[i][j] != 'F':
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + int(grid[i][j])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # The result is stored in the bottom-right cell of the dp array
    return dp[rows-1][cols-1]

# Given input
input_grid = [
    [2, 0, 1, 1, 'F'],
    [1, 2, 0, 2, 3],
    [2, 2, 0, 2, 1],
    [3, 1, 0, 2, 0],
    ['S', 0, 1, 3, 0]
]

# Find and print the maximum sum
result = find_maximum_sum(input_grid)
print(result)
