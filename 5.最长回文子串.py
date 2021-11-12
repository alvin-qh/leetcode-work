#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:

    def longestPalindrome(self, s: str) -> str:
        """
        Args:
            s(str): 输入的字符串

        Returns:
            str: 输入字符串包含的最大回文子字符串
        """
        s_dict = {}
        last_rs = ''
        for i, c in enumerate(s):
            if c in s_dict:
                s_dict[c].append(i)
            else:
                s_dict[c] = [i]

            for n in s_dict[c]:
                if i + 1 - n > len(last_rs):
                    fs = s[n:i + 1]
                    if fs == fs[::-1]:
                        last_rs = fs

        return last_rs
# @lc code=end
