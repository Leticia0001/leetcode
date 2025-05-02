def countWays(stepsLeft):
    if stepsLeft == 0:
        return 1  
    if stepsLeft < 0:
        return 0  
    return countWays(stepsLeft - 1) + countWays(stepsLeft - 2)

print(countWays(4))  # Output: 5
