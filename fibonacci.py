# Time Complexity = O(2^n)
# Space Complexity = O(n)
def fibonacci_brute_force(n):
    if n <= 2:
        return 1

    return fibonacci_brute_force(n - 1) + fibonacci_brute_force(n - 2)


# Time Complexity = O(n)
# Space Complexity = O(n)
def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1

    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]


# Time Complexity = O(n)
# Space Complexity = O(n)
def fibonacci_tabulated(n):
    table = [0] * (n + 1)
    table[1] = 1
    
    for i in range(n - 1):
        table[i + 1] += table[i]
        table[i + 2] += table[i]
    table[-1] += table[-2]

    return table[n]


if __name__ == '__main__':
    print(fibonacci_brute_force(1)) #1
    print(fibonacci_brute_force(2)) #1
    print(fibonacci_memoized(4)) #3
    print(fibonacci_memoized(7)) #13
    print(fibonacci_tabulated(50)) #12586269025
