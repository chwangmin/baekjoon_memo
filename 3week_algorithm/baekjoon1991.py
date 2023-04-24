import sys

input = sys.stdin.readline

# 노드 정렬
class Node:
    def __init__(self,item):
        # 자기 값 가져와서 item으로 정의
        self.item=item
        # 왼쪽, 오른쪽 초기 값은 None으로
        self.left=None
        self.right=None

# 트리로 만들기
class BinaryTree():
    def __init__(self):
        self.root = None

    def preOrder(self, n):
        if n != None:
            print(n.item,'',end='')
            if n.left:
                self.preOrder(n.left)
            if n.right:
                self.preOrder(n.right)

tree_num = int(input())

for i in range(tree_num):
    root, left, right = input().split()
    
    Node(root).left = Node(left)
    Node(root).right = Node(right)

tree = BinaryTree()
tree.root = Node('A')
    
def inOrder():
    return

def postOrder():
    return

tree.preOrder(tree.root)