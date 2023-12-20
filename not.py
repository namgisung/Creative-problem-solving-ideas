def find_maximum_sum(grid):
    rows = len(grid)
    cols = len(grid[0])

    
    dp = [[0] * cols for _ in range(rows)]


    for j in range(cols):
        if grid[0][j] != 'S':
            dp[0][j] += int(grid[0][j])

    
    for j in range(1, cols):
        if grid[0][j] == 'F':
            dp[0][j] = dp[0][j-1]
        elif grid[0][j] != 'S':
            dp[0][j] = dp[0][j-1] + int(grid[0][j])
        else:
            dp[0][j] = dp[0][j-1]

    
    for i in range(1, rows):
        if grid[i][0] == 'F':
            dp[i][0] = dp[i-1][0]
        elif grid[i][0] != 'S':
            dp[i][0] = dp[i-1][0] + int(grid[i][0])
        else:
            dp[i][0] = dp[i-1][0]

    
    for i in range(1, rows):
        for j in range(1, cols):
            if grid[i][j] == 'F':
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            elif grid[i][j] != 'S':
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + int(grid[i][j])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    
    return dp[rows-1][cols-1]


input_grid = [
    ['S', 0, 1, 3, 0],
    [3, 1, 0, 2, 0],
    [2, 2, 0, 2, 1],
    [1, 2, 0, 2, 3],
    [2, 0, 1, 1, 'F']
]

result = find_maximum_sum(input_grid)
print(result)

#Initial dp array:
#[2, 0, 1, 1, 0]
#[0, 0, 0, 0, 0]
#[0, 0, 0, 0, 0]
#[0, 0, 0, 0, 0]
#[0, 0, 0, 0, 0]

#After initializing the first row:
#[2, 2, 3, 4, 4]
#[0, 0, 0, 0, 0]
#[0, 0, 0, 0, 0]
#[0, 0, 0, 0, 0]
#[0, 0, 0, 0, 0]

#After initializing the first column:
#[2, 2, 3, 4, 4]
#[3, 0, 0, 0, 0]
#[5, 0, 0, 0, 0]
#[8, 0, 0, 0, 0]
#[8, 0, 0, 0, 0]

#Final dp array:
#[2, 2, 3, 4, 4]
#[3, 5, 5, 7, 10]
#[5, 7, 7, 9, 11]
#[8, 9, 9, 11, 11]
#[8, 9, 10, 14, 14]

#14
