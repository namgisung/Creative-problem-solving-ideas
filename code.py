def find_maximum_sum(grid):
    rows = len(grid)
    cols = len(grid[0])

    
    dp = [[0] * cols for _ in range(rows)]


    for j in range(cols):
        if grid[0][j] != 'F':
            dp[0][j] += int(grid[0][j])

    
    for j in range(1, cols):
        if grid[0][j] == 'S':
            dp[0][j] = dp[0][j-1]
        elif grid[0][j] != 'F':
            dp[0][j] = dp[0][j-1] + int(grid[0][j])
        else:
            dp[0][j] = dp[0][j-1]

    
    for i in range(1, rows):
        if grid[i][0] == 'S':
            dp[i][0] = dp[i-1][0]
        elif grid[i][0] != 'F':
            dp[i][0] = dp[i-1][0] + int(grid[i][0])
        else:
            dp[i][0] = dp[i-1][0]

    
    for i in range(1, rows):
        for j in range(1, cols):
            if grid[i][j] == 'S':
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            elif grid[i][j] != 'F':
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + int(grid[i][j])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    
    return dp[rows-1][cols-1]


input_grid = [
    [2, 0, 1, 1, 'F'],
    [1, 2, 0, 2, 3],
    [2, 2, 0, 2, 1],
    [3, 1, 0, 2, 0],
    ['S', 0, 1, 3, 0]
]

result = find_maximum_sum(input_grid)
print(result)

