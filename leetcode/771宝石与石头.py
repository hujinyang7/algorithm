'''
给你一个字符串 jewels 代表石头中宝石的类型，另有一个字符串 stones 代表你拥有的石头。 
stones 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。
字母区分大小写，因此 "a" 和 "A" 是不同类型的石头

示例 1：
输入：jewels = "aA", stones = "aAAbbbb"
输出：3

示例 2：
输入：jewels = "z", stones = "ZZ"
输出：0
'''


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for s in stones:
            if s in jewels:
                count += 1
        return count
