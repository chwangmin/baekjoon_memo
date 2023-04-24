# self 는 아껴쓰자 생각보다 속도 차이가 남.

import sys

sys.setrecursionlimit(100000)

input = sys.stdin.readline

class Node:
    def __init__(self, item)->None:
        self.item = item
        self.left = None
        self.right = None

class Tree():
    def __init__(self)->None:
        self.root = None
    
    def append(self,num)->bool:
        newNode = Node(num)

        if self.root == None:
            self.root = newNode
        else:
            current = self.root

            while True:
                if num < current.item:
                    if current.left is not None:
                        current = current.left
                    else:
                        current.left = newNode
                        break

                else:
                    if current.right is not None:
                        current = current.right
                    else:
                        current.right = newNode
                        break

    def PostOrder(self, now):
        if not now.left == None:
            self.PostOrder(now.left)
        if not now.right == None:
            self.PostOrder(now.right)
        print(now.item)

num_list = [int(s.rstrip()) for s in sys.stdin.readlines()]

tree = Tree()

for i in num_list:
    tree.append(i)

tree.PostOrder(tree.root)

