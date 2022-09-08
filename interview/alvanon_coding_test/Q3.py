# coding:utf-8
# @Time: 8/28/2022
# @Author: hujinyang
# @Email: hujinyang4@163.com
# @File: Q3.py
# @Project: alvanon_coding_test


class Stack():
    def __init__(self):
        self.__list = []

    def push(self, value):
        self.__list.append(value)

    def pop(self):
        if self.__list:
            return self.__list.pop()
        return None

    def inc(self, length, value):
        if length <= 0:
            return
        elif length >= len(self.__list):
            self.__list = [each + value for each in self.__list]
        else:
            for i in range(length):
                self.__list[i] += value

    def peek(self):
        if self.__list:
            return self.__list[-1]
        return 'EMPTY'



if __name__ == '__main__':
    stack = Stack()
    print (stack.peek())   # EMPTY
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    print (stack.peek())   # 6
    print (stack.pop())    # 6
    print (stack.peek())   # 5
    stack.inc(-1, 10)   # 当需要 increase 的个数为负，栈内元素保持不变
    print (stack.peek())   # 5
    print (stack._Stack__list)   # [1, 2, 3, 4, 5]
    stack.inc(10, 10)   # 当需要 increase 的个数超过栈内元素长度，对栈内所有元素执行操作
    print (stack.peek())   # 15
    print (stack._Stack__list)   # [11, 12, 13, 14, 15]
    stack.inc(3, 5)   # 对栈内部分元素 increase 操作
    print (stack.peek())   # 15
    print (stack._Stack__list)   # [16, 17, 18, 14, 15]
