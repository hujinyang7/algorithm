'''
请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）
实现 MyQueue 类：
void push(int x) 将元素 x 推到队列的末尾
int pop() 从队列的开头移除并返回元素
int peek() 返回队列开头的元素
boolean empty() 如果队列为空，返回 true ；否则，返回 false
说明：
你 只能 使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。

'''


class Stack():
    def __init__(self):
        self.__list = []

    def push(self,item):
        self.__list.append(item)

    def pop(self):
        return self.__list.pop()

    def peek(self):
        if  self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)



class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.push(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.s2.is_empty():
            return self.s2.pop()
        while not self.s1.is_empty():
            val = self.s1.pop()
            self.s2.push(val)
        return self.s2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.s2.is_empty():
            return self.s2.peek()
        while not self.s1.is_empty():
            val = self.s1.pop()
            self.s2.push(val)
        return self.s2.peek()


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.s1.is_empty() and self.s2.is_empty()
