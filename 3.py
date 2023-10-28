def climbStairsRecursive(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return climbStairsRecursive(n - 1) + climbStairsRecursive(n - 2)

# Виклик функції і виведення результату
n = 3
result = climbStairsRecursive(n)
print(result)


