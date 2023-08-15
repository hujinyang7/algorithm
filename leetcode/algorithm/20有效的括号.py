'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
 

示例 1：
输入：s = "()"
输出：true

示例 2：
输入：s = "()[]{}"
输出：true

示例 3：
输入：s = "(]"
输出：false

示例 4：
输入：s = "([)]"
输出：false

示例 5：
输入：s = "{[]}"
输出：true
'''



class Solution:
    brackets = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for each in s:
            # 右括号弹出对应左括号
            if each in self.brackets:
                if not stack or stack[-1] != self.brackets.get(each):
                    return False
                stack.pop()
            # 左括号入栈
            else:
                stack.append(each)
        # 结束判断栈里面是否有值
        return not stack
