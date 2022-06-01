def can_construct(target_str, word_bank, memo=None):
    """
    This function determines if the given word can be constructed using the word bank.
    Time complexity: O(n*m^2) where m is the target string and n is the length of the word bank
    Space complexity: O(m*m) where m is the target string and need to store the remainder
    string as well
    :param target_str: str
    :param word_bank: List[str]
    :param memo: dict
    :return: bool
    """
    if memo is None:
        memo = dict()
    if target_str in memo:
        return memo[target_str]
    if target_str == '':
        return True
    for word in word_bank:
        try:
            if target_str.index(word) == 0:
                remainder_str = target_str[len(word):]
                if can_construct(remainder_str, word_bank, memo):
                    memo[target_str] = True
                    return memo[target_str]
        except ValueError:
            continue
    memo[target_str] = False
    return False


if __name__ == '__main__':
    print(can_construct('skateboard', ['ska', 'te', 'boar', 'sk', 'board', 'a', 'te']))