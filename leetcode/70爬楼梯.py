'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？


 示例 1：
输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶

示例 2：
输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
'''



class Solution:
    '''
    n=1: 1    共1种
    n=2: 1 2  共2种
    n=3: 111  12  21  共3种
    n=4: 1111  112  121  211  22  共5种
    n=5: 11111  1112  1121  1211  122  2111  212  221  共8种
    斐波那契数列
    '''
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for i in range(n-2):
            a, b = b, a+b
        return b
