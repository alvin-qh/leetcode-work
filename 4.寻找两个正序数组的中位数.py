#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
from typing import List


# @lc code=start
class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        算法思路:
            最基本的算法，可以将两个数组连接后排序即可
                对于数组元素为奇数，找到中间位置的值即可
                对于数组元素格式为偶数，则是中间位置的两个数的平均数

            连接数组并排序会耗费额外的内存空间和，所以可以用两个指针来模拟数组合并排序

            通过 mid = len(nums1) + len(nums2) 计算出数组合并后的中间位置
            另 i 指向 nums1 数组，j 指向 nums2 数组，mid 表示中间位置
            将 i + j == mid + 1 作为迭代结束的条件，即已定位到中间位置
            在迭代过程中，通过判断连个指针是否指向各自数组的末尾和指向元素的大小比较来确定 i 和 j 指针的移动

        Args:
            nums1(List[int]): 第一个有序数组
            nums2(List[int]): 第二个有序数组

        Returns:
            float: 两个数组的中位数
        """
        total_len = len(nums1) + len(nums2)

        # i, j 表示指向 num1 和 num2 数组的两个指针
        # mid 表示若两个数组合并后，中间位置的索引
        i, j, mid = 0, 0, (total_len + 1) // 2
        
        # 计算中位数的左值和右值
        left, right = 0, 0

        while i + j < mid + 1:
            a = nums1[i] if i < len(nums1) else None  # 获取 i 指针指向的元素值
            b = nums2[j] if j < len(nums2) else None  # 获取 j 指针指向的元素值

            if a is None:  # 判断 i 指针是否已到达 num1 数组末尾，跳过 num1 数组，移动 j 指针
                val = b
                j += 1
            elif b is None:  # 判断 j 指针是否已到达 num2 数组末尾，忽略 num2 数组，移动 i 指针
                val = a
                i += 1
            else:
                if a > b:  # 两个指针都有效时，比较两个指针指向的元素值，并移动对应的指针
                    val = b
                    j += 1
                else:
                    val = a
                    i += 1

            # 总索引值（即 i + j) 在 mid 或之前时，给左值赋值，超过 mid 后，给右值复制，此时循环结束
            if i + j == mid:
                left = val
            elif i + j == mid + 1:
                right = val

        return (left + right) / 2 if total_len % 2 == 0 else left
# @lc code=end

