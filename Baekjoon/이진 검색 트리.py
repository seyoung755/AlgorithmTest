import sys

sys.setrecursionlimit(10 ** 6)
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, node, data):
        self.root = self._insert_value(self.root, data)

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        
        else:
            if data < node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        
        return node

    def pre_order(self, root):
        if root is None:
            pass
        else:
            print(root.data)
            self.pre_order(root.left)
            self.pre_order(root.right)

    def post_order(self, root):
        if root is None:
            pass
        else:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.data)

    def post_order_traversal(self):
        def _post_order_traversal(root):
            if root is None:
                pass
            else:
                _post_order_traversal(root.left)
                _post_order_traversal(root.right)
                print(root.data)
        _post_order_traversal(self.root)


def post_order(start, end):

    if start > end:
        return

    # print(pre_order[start:end+1])

    root = pre_order[start]
    idx = start+1

    while idx <= end:
        # 오른쪽 서브트리를 만났을 때
        if pre_order[idx] > root:
            break
        idx += 1
    # 왼쪽 서브트리부터 조사
    post_order(start+1, idx-1)

    # 오른쪽 서브트리 조사
    post_order(idx, end)

    # 마지막에 현재 노드 출력
    print(root)


bt = BinaryTree()
pre_order = []

while True:
    try:
        data = int(input())
        pre_order.append(data)
    except:
        break

post_order(0, len(pre_order)-1)
