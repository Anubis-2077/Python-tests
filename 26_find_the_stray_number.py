"""You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Complete the method which accepts such an array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)"""

from collections import Counter


def stray(arr):
    print(Counter(arr))
    return [number for number, frequency in Counter(arr).items() if frequency == 1][0]


print(stray([1, 1, 1, 1, 2, 1, 1, 1]))
