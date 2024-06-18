#!/usr/bin/python3
"""Maria and Ben are playing a game"""


def isWinner(x, nums):
    """x - rounds of the game
    nums - array of n
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    Ben = 0
    Maria = 0

    j = [1 for x in range(sorted(nums)[-1] + 1)]
    j[0], j[1] = 0, 0
    for i in range(2, len(j)):
        rm_multiples(j, i)

    for i in nums:
        if sum(j[0:i + 1]) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Ben > Maria:
        return "Ben"
    if Maria > Ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """takes away multiple
    of primes
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
