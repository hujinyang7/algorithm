'''
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数
例如，121 是回文，而 123 不是
'''


class Solution():
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        beg = 0
        end = len(s)-1
        while beg < end:
            if s[beg] == s[end]:
                beg += 1
                end -= 1
            else:
                return False
        return True

    def _isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
