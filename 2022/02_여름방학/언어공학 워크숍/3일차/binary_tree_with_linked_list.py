# 연결 자료 구조를 이용한 이진 트리(Binary Tree) 구현

class Node:
    def __init__(
        self,
        value: int | str,
        left: 'Node' = None,
        right: 'Node' = None
    ) -> None:
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root: 'Node') -> None:
        self.root = root


if __name__ == "__main__":
    n7: Node = Node(value=7)
    n6: Node = Node(value=6)
    n5: Node = Node(value=5)
    n4: Node = Node(value=4)
    n3: Node = Node(value=3, left=n6, right=n7)
    n2: Node = Node(value=2, left=n4, right=n5)
    n1: Node = Node(value=1, left=n2, right=n3)
    binary_tree: Tree = Tree(root=n1)
    
    # Print left child node of the root node.
    print(n3.value)
    print(binary_tree.root.left.value)

    node_d: Node = Node(value="D")
    node_c: Node = Node(value="C", left=node_d)
    node_b: Node = Node(value="B", left=node_c)
    node_a: Node = Node(value="A", left=node_b)
    left_skewed_binary_tree: Tree = Tree(root=node_a)
    
    left_skewed_binary_node: Node = left_skewed_binary_tree.root
    while left_skewed_binary_node:
        # Print from the root node to leaf node.
        print(left_skewed_binary_node.value)
        left_skewed_binary_node = left_skewed_binary_node.left
        
    