def can_sum(target_sum, numbers, memo=None):
    """
    This function checks if the numbers provided in the array can add up to the target sum.
    Time complexity: O(m*n) where m is the target sum and n is the number of array elements
    Space complexity: O(m) for storing the memo
    :param target_sum: int
    :param numbers: list
    :param memo: dict
    :return: bool
    """
    if memo is None:
        memo = dict()
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    for num in numbers:
        remainder = target_sum - num
        if can_sum(remainder, numbers, memo):
            memo[target_sum] = True
            return memo[target_sum]
    memo[target_sum] = False
    return False


if __name__ == '__main__':
    print(can_sum(300, [7, 14]))