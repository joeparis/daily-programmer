#!/usr/bin/env python3

# https://www.reddit.com/r/dailyprogrammer/comments/83uvey/20180312_challenge_354_easy_integer_complexity_1/

from math import sqrt, floor


def integer_complexity(a):
    factors = []

    for b in range(1, floor(sqrt(a))):
        if a % b == 0:
            factors.append((b, a // b))

    # for n in factors:
    #     print(f"{a} = {n[0]}*{n[1]}")

    sums = [n[0] + n[1] for n in factors]

    print(f"{a}  =>  {min(sums)}")


if __name__ == '__main__':
    nums = [12, 456, 4567, 12345, 345678]

    for num in nums:
        integer_complexity(num)
