import sys

input = sys.stdin.readline

class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class Tree():
    def __init__(self,start,left,right):
        self.root = Node(start)
        if left != '.':
            self.root.left = Node(left)
        if right != '.':
            self.root.right = Node(right)
    def append(self, parent, left, right):
        current = self.root
        stack = []
        if self.root.right:
            stack.append((parent,left,right,current))
        if self.root.left:
            stack.append((parent,left,right, current))
        while stack:
            parent, left, right, current = stack.pop()
            if parent == current.item:
                if left != '.':
                    current.left = Node(left)
                if right != '.':
                    current.right = Node(right)
                return
            if current.right:
                stack.append((parent,left,right,current.right))
            if current.left:
                stack.append((parent,left,right,current.left))

    def preOrder(self, start):
        print(start.item, end = '')
        if start.left:
            self.preOrder(start.left)
        if start.right:
            self.preOrder(start.right)

    def inOrder(self, start):
        if start.left:
            self.inOrder(start.left)
        print(start.item, end = '')
        if start.right:
            self.inOrder(start.right)
    
    def postOrder(self, start):
        if start.left:
            self.postOrder(start.left)
        if start.right:
            self.postOrder(start.right)
        print(start.item, end = '')

num = int(input())

tree_list = []

for i in range(num):
    a, b, c = map(str, input().split())
    
    tree_list.append((a,b,c))

tree = Tree(tree_list[0][0],tree_list[0][1], tree_list[0][2])

for i in range(1, num):
    tree.append(tree_list[i][0],tree_list[i][1], tree_list[i][2]) 

tree.preOrder(tree.root)
print()
tree.inOrder(tree.root)
print()
tree.postOrder(tree.root)