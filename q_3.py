"""
3. 无重复字符的最长子串
    给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

    示例 1:
        输入: "abcabcbb"
        输出: 3
        解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

    示例 2:
        输入: "bbbbb"
        输出: 1
        解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

    示例 3:
        输入: "pwwkew"
        输出: 3
        解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。

    请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""


def length_of_longest_substring(s: str) -> int:
    cs = set()
    ml = 0
    i, j = 0, 0
    while i < len(s) and j < len(s):
        if s[i] not in cs:
            cs.add(s[i])
            i += 1
            ml = max(ml, i - j)
        else:
            cs.remove(s[j])
            j += 1
    return ml


def test_solution():
    assert length_of_longest_substring('aab') == 2
    assert length_of_longest_substring(' ') == 1
    assert length_of_longest_substring('abcabcbb') == 3
