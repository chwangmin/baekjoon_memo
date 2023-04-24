import sys

input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self,root,left,right):
        self.root = Node(root)
        if left != '.':
            self.root.left = Node(left)
        if right != '.':
            self.root.right = Node(right)
    
    def append(self,parent,left,right):
        self.current = self.root
        stack = []
        if self.current.right:
            stack.append(self.current.right)
        if self.current.left:
            stack.append(self.current.left)
        while stack:
            self.current = stack.pop()
            if self.current.data == parent:
                if left != '.':
                    self.current.left = Node(left)
                if right != '.':
                    self.current.right = Node(right)
                return
            if self.currnt.right:
                stack.append(self.current.right)
            if self.current.left:
                stack.append(self.current.left)
        
    def PreOrder(self, now):
        print(now.data, end='')
        if now.left:
            self.PreOrder(now.left)
        if now.right:
            self.PreOrder(now.right)
    
    def InOrder(self, now):
        if now.left:
            self.InOrder(now.left)
        print(now.data, end='')
        if now.right:
            self.InOrder(now.right)

    def PostOrder(self, now):
        if now.left:
            self.PostOrder(now.left)
        if now.right:
            self.PostOrder(now.right)
        print(now.data, end='')