class Node:
    def __init__(
        self,
        value: str,
        left: "Node" = None,
        right: "Node" = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right
        

class Tree:
    def __init__(self, root: Node) -> None:
        self.root: Node = root

    def preorder_traversal(self, node: Node) -> None:
        if node:
            print(node.value, end="")
            self.preorder_traversal(node=node.left)
            self.preorder_traversal(node=node.right)
        
        else:
            return None
        
        
    def inorder_traversal(self, node: Node) -> None:
        if node:
            self.inorder_traversal(node=node.left)
            print(node.value, end="")
            self.inorder_traversal(node=node.right)
                
        else:
            return None
    
    
    def postorder_traversal(self, node: Node) -> None:
        if node:
            self.postorder_traversal(node=node.left)
            self.postorder_traversal(node=node.right)
            print(node.value, end="")
                
        else:
            return None        


if __name__ == "__main__":
    """
    수식 `A*B - C/D`에 대한 이진 트리를 생성하고 전위 순회, 중위 순회, 후위 순회를 차례로 수행하면서 순회경로를 출력하는 메서드를 작성하시오.
    """
    n7: Node = Node(value="D")
    n6: Node = Node(value="C")
    n5: Node = Node(value="/", left=n6, right=n7)
    n4: Node = Node(value="B")
    n3: Node = Node(value="A")
    n2: Node = Node(value="*", left=n3, right=n4)
    n1: Node = Node(value="-", left=n2, right=n5)
    
    tree: Tree = Tree(root=n1)
    
    print("Preorder Traversal: ", end="")
    tree.preorder_traversal(node=tree.root)
    print("\nInorder Traversal: ", end="")
    tree.inorder_traversal(node=tree.root)
    print("\nPostorder Traversal: ", end="")
    tree.postorder_traversal(node=tree.root)
