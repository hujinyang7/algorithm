# coding:utf-8

class Node():
    """节点类"""
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Tree():
    def __init__(self):
        """二叉树"""
        self.root = None

    def add(self, item):
        node = Node(item)
        if not self.root:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if not cur_node.left:
                cur_node.left = node
                return
            else:
                queue.append(cur_node.left)
            if not cur_node.right:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)

    def breadth_travel(self):
        """广度遍历"""
        if not self.root:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.value, end=',')
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)

    def pre_order(self, node):
        """先序遍历"""
        if not node:
            return
        print(node.value, end=',')
        self.pre_order(node.left)
        self.pre_order(node.right)

    def in_order(self, node):
        """中序遍历"""
        if not node:
            return
        self.in_order(node.left)
        print(node.value, end=',')
        self.in_order(node.right)

    def post_order(self, node):
        """后序遍历"""
        if not node:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.value, end=',')


if __name__ == "__main__":
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print(" ")
    tree.pre_order(tree.root)
    print(" ")
    tree.in_order(tree.root)
    print(" ")
    tree.post_order(tree.root)
    print(" ")
