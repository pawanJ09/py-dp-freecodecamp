def how_sum(target_sum, numbers, memo=None):
    """
    This function finds the first match of numbers from the list that matches the target sum.
    Time Complexity: O(n^m*m) where m is the target sum and n is the number of elements in the
    list and the second m is the time required to append to the result array
    Space complexity: O(m*m) where m is the stack of the target sum for recursion and result array
    :param target_sum: int
    :param numbers: list
    :param memo: dict
    :return: list
    """
    if memo is None:
        memo = dict()
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    for num in numbers:
        remainder = target_sum - num
        result = how_sum(remainder, numbers, memo)
        if result is not None:
            memo[target_sum] = result.append(num)
            return result
    memo[target_sum] = None
    return None


if __name__ == '__main__':
    print(how_sum(7, [5, 4, 4, 1]))
    print(how_sum(300, [7, 14]))