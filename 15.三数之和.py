#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
from typing import List


# @lc code=start
class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        算法说明:
            对数组进行排序，这样才能保证查找过程中不会访问到重复值
            三个指针 a, b, c，分别指向 第一个加数（从 0 下标开始），第二个加数（从 a + 1 开始），第三个加数（从数组末尾开始）

            因为数组有序，所以 b > a, c > b 成立，因为之前的元素都已经枚举过

        Args:
            nums(List[int]): 输入的字符串数组

        Returns:
            List[List[int]]: 返回所有字符串公共的前缀
        """
        res = []

        nums.sort()

        # i, a, b 分别为三个指针:
        #    i 依次指向数组的每个元素
        #    a, b 为双指针，指向 i 之后的元素，a 从左到右，b 从右到左
        # 因为数组是有序的，所以 a 和 b 指针无需重合

        # 遍历 i 指针
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  # 排除 i 指针指向相邻的重复值情况
                continue

            a, b = i + 1, len(nums) - 1  # 计算 b 指针，b 指针指向数组末尾
            t = -nums[i]  # 计算 a + b 的期望值 （t = 0 - nums[i]）

            # 遍历 a 指针，从 i 指针之后到数组结束
            for a in range(i + 1, len(nums) - 1):
                if a < b and nums[a] == nums[a - 1]:  # 排除 a 指针执行相邻重复值情况
                    continue

                # 遍历 b 指针
                while b > a and nums[b] + nums[a] > t:  # 判断 c 值是否符合条件
                    b -= 1

                # 如果 b 和 c 重合，此迭代找寻失败
                if a == b:
                    break

                # 记录查找结果
                if nums[a] + nums[b] == t:
                    res.append([nums[i], nums[a], nums[b]])

        return res
# @lc code=end
