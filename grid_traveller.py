def grid_traveller(m, n, memo=None):
    """
    Function to find the number of possible ways to travel in grid.
    Time Complexity: O(m*n) where m and n are rows/cols of the grid
    Space complexity: O(n+m) since this is a 2D grid
    :param m: int
    :param n: int
    :param memo: dict
    :return: int
    """
    # Form a key from m, n to add to the memo
    key = str(m) + ',' + str(n)
    if memo is None:
        memo = dict()
    if key in memo:
        return memo[key]
    # Check base cases
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    memo[key] = grid_traveller(m - 1, n, memo) + grid_traveller(m, n - 1, memo)
    return memo[key]


if __name__ == '__main__':
    print(grid_traveller(18, 18))
