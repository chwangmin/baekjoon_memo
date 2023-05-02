import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

class Node:
    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None

class Tree:
    def __init__(self,number):
        self.root = Node(number)
    def append(self,number):
        current = self.root
        while True:
            if number <= current.item:
                if not current.left:
                    current.left = Node(number)
                    return
                current = current.left
            else:
                if not current.right:
                    current.right = Node(number)
                    return
                current = current.right

    def postOrder(self, start):
        if start.left:
            self.postOrder(start.left)
        if start.right:
            self.postOrder(start.right)
        print(start.item)


list_tree = []

while True:
    try:
        list_tree.append(int(input()))
    except:
        break

tree = Tree(list_tree[0])

for i in range(1,len(list_tree)):
    tree.append(list_tree[i])

tree.postOrder(tree.root)