"""
4. 寻找两个有序数组的中位数
    给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
    请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

    你可以假设 nums1 和 nums2 不会同时为空。

    示例 1:
        nums1 = [1, 3]
        nums2 = [2]
        则中位数是 2.0

    示例 2:
        nums1 = [1, 2]
        nums2 = [3, 4]
        则中位数是 (2 + 3) / 2 = 2.5
"""

from typing import List


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    total_len = len(nums1) + len(nums2)
    i, j, n, mid = 0, 0, 0, (len(nums1) + len(nums2) + 1) // 2
    left, right = 0, 0
    while n < mid + 1:
        a = None
        if i < len(nums1):
            a = nums1[i]

        b = None
        if j < len(nums2):
            b = nums2[j]

        if a is None:
            val = b
            j += 1
        elif b is None:
            val = a
            i += 1
        else:
            if a > b:
                val = b
                j += 1
            else:
                val = a
                i += 1

        if n == mid - 1:
            left = val
        elif n == mid:
            right = val

        n += 1

    if total_len % 2 == 0:
        mid = (left + right) / 2
    else:
        mid = left

    return mid


def test_solution():
    assert find_median_sorted_arrays([1, 3], [2]) == 2
    assert find_median_sorted_arrays([1, 2], [3, 4]) == 2.5
