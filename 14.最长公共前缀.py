#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
from typing import List


# @lc code=start
class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        算法思路：
            从第一个字符串 s0 的第 i 位置获取字符 c
            判断后续字符串 s1, s2, ..., sn 的第 i 个字符是否为 c
            如果是，则从 i + 1 继续迭代
            否则，前 i 个字符组成公共前缀

        Args:
            strs(List[str]): 输入的字符串数组

        Returns:
            str: 返回所有字符串公共的前缀
        """
        if len(strs) == 0:
            return ''

        res = []
        for i in range(0, min(len(s) for s in strs)):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if c != strs[j][i]:
                    return ''.join(res)

            res.append(c)

        return ''.join(res)
# @lc code=end

