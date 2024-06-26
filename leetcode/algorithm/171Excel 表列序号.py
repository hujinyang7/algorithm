'''
给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。返回 该列名称对应的列序号

例如：
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...

示例 1:
输入: columnTitle = "A"
输出: 1

示例 2:
输入: columnTitle = "AB"
输出: 28

示例 3:
输入: columnTitle = "ZY"
输出: 701
'''


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for i in columnTitle:
            res = res * 26 + ord(i) - 64
        return res
