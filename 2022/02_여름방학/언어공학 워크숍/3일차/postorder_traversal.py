# 후위 순회(Postorder Traversal) 구현

class Node:
    def __init__(
        self,
        value: int | str,
        left: "Node" = None,
        right: "Node" = None,
        index: int = -1
    ) -> None:
        self.value = value
        self.index = index
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root: "Node") -> None:
        self.root = root


def postorder_traversal(visit: list[int], dp: list[bool], node: "Node"):
    if node and not dp[node.index]:
        postorder_traversal(visit=visit, dp=dp, node=node.left)
        postorder_traversal(visit=visit, dp=dp, node=node.right)
        dp[node.index] = True
        visit.append(node.value)
    
    else:
        return None


if __name__ == "__main__":
    n7: Node = Node(value=7, index=7)
    n6: Node = Node(value=6, index=6)
    n5: Node = Node(value=5, index=5)
    n4: Node = Node(value=4, index=4)
    n3: Node = Node(value=3, left=n6, right=n7, index=3)
    n2: Node = Node(value=2, left=n4, right=n5, index=2)
    n1: Node = Node(value=1, left=n2, right=n3, index=1)
    binary_tree: Tree = Tree(root=n1)
    
    
    visit: list[int] = [None]
    dp: list[bool] = [False] * 8
    postorder_traversal(visit=visit, dp=dp, node=binary_tree.root)
    print(visit)
    print(dp)
    
    