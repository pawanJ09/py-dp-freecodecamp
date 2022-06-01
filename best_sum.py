def best_sum(target_sum, numbers, memo=None):
    if memo is None:
        memo = dict()
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    best_result = None
    for num in numbers:
        remainder = target_sum - num
        result = best_sum(remainder, numbers, memo)
        if result is not None:
            res = [r for r in result]
            res.append(num)
            if best_result is None or len(best_result) > len(res):
                best_result = res
    memo[target_sum] = best_result
    return best_result


if __name__ == '__main__':
    print(best_sum(7, [5, 4, 4, 1]))
    print(best_sum(100, [7, 5, 25]))
    print(best_sum(21, [2, 4]))

