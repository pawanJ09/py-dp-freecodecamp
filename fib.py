def fib(n, memo=None):
    """
    Function to find fibonacci number at nth location.
    Time Complexity: O(n) where n is the position
    Space Complexity: O(n) where n is the size of the memo
    :param n: int
    :param memo: dict
    :return: int
    """
    if memo is None:
        memo = dict()
    if n in memo:
        return memo[n]
    if 2 >= n >= 1:
        return 1
    elif n == 0:
        return 0
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


if __name__ == '__main__':
    print(fib(50))