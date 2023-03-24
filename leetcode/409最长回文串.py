'''
给定一个包含大写字母和小写字母的字符串 s ，返回 通过这些字母构造成的 最长的回文串 。
在构造过程中，请注意 区分大小写 。比如 "Aa" 不能当做一个回文字符串。

示例 1:
输入:s = "abccccdd"
输出:7
解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。

示例 2:
输入:s = "a"
输出:1

示例 3：
输入:s = "aaaaaccc"
输出:7
'''


class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        counter = Counter(s)
        res, mid = 0, 0
        for count in counter.values():
            # 如果 count 是奇数，tmp就会得1，那 i-tmp 就会变成偶数
            # 如果 count 是偶数，tmp就会得0，那 i-tmp 就还是偶数
            tmp = count % 2
            res += count - tmp
            if tmp == 1:
                mid = 1
        return res + mid
