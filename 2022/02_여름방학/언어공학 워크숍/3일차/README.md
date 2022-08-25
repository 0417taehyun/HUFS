# 3일차: 비선형 자료 구조 트리(Tree)

## 목차

- [학습 목표](#학습-목표)
- [비선형 자료 구조: 트리(Tree)](#비선형-자료-구조-트리tree)
  - [구현](#구현)
  - [이진 트리의 순회(Traverse)](#이진-트리의-순회traversal)
  - [트리 순회의 응용](#트리-순회의-응용)
  - [이진 탐색 트리](#이진-탐색-트리)
- [실습](#실습)

### 학습 목표

- 비선형 자료 구조 트리(Tree)

### 비선형 자료 구조: 트리(Tree)

#### 구현

##### 1차원 배열의 순차 자료 구조 사용

높이가 H인 포화 이진 트리의 노드번호를 배열의 인덱스로 사용하는 방법이다.

이때 인덱스 0번은 실제로 사용하지 않고 비워두며 루트 노드는 인덱스 1번부터 시작한다.

1차원 배열로 이진 트리를 구현할 경우 각 노드의 인덱스 관계는 아래 표와 같다.

이때 N은 배열의 크기를 의미한다.

<table>
    <tr>
        <th> 노드 </th>
        <th> 인덱스 </th>
        <th> 성립 조건 </th>
    </tr>
    <tr>
        <td> 노드 i의 부모 노드 </td>
        <td> i//2 </td>
        <td> i > 1 </td>
    </tr>
    <tr>
        <td> 노드 i의 왼쪽 자식 노드 </td>
        <td> 2*i </td>
        <td> 2*i <= N </td>
    </tr>
    <tr>
        <td> 노드 i의 오른쪽 자식 노드 </td>
        <td> (2*i)+1 </td>
        <td> (2*i)+1 <= N </td>
    </tr>
    <tr>
        <td> 루트 노드 </td>
        <td> 1 </td>
        <td> N > 0 </td>
    </tr>            
</table>

그러나 이러한 구현은 메모리 관리에 있어 비효율성이 존재한다.

예를 들어 편향 이진 트리를 구현할 경우 사용하지 않은 배열 원소에 대한 메모리 공간에 낭비가 발생하기 때문이다.

더욱이 트리의 원소를 삽입하거나 삭제할 때 배열의 크기를 변경하기 어려움이 있다.

##### 연결 자료 구조를 이용한 이진 트리의 구현

모든 노드들이 가지는 공통 정보가 총 세 가지다.

1. 값
2. 왼쪽 자식 노드의 주소
3. 오른쪽 자식 노드의 주소

모든 트리가 가지는 공통 정보는 한 가지이다.

1. 루트 노드

이러한 부분을 활용하여 아래와 같이 연결 자료 구조 형태로 이진 트리를 구현할 수 있다.

```Python
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
```

#### 이진 트리의 순회(Traversal)

계층적 구조로 저장되어 있는 트리의 모든 노드를 방문하여 데이터를 처리하는 연산을 의미한다.

다시 말해 트리 구조로 저장된 데이터를 탐색하는 방법이다.

우선 순회를 위해 수행할 수 있는 작업을 정의해야 한다.

1. 현재 노드를 방문하여 데이터를 읽는 작업
2. 현재 노드의 왼쪽 서브 트리로 이동하는 작업
3. 현재 노드의 오른쪽 서브 트리로 이동하는 작업

이때 중요한 점은 왼쪽 자식 노드를 먼저 방문한 다음 오른쪽 자식 노드를 방문한다.

이러한 순회의 종류는 아래와 같이 세 가지가 있다.

1. 전위 순회(Preorder Traversal)
2. 중위 순회(Inorder Traversal)
3. 후위 순회(Postorder Traversal)

이때 유의할 점은 전위 순회와 후위 순회는 본인을 언제 방문할 것인지 결정되어 있기 때문에 -전위 순회의 경우 가장 먼저, 후위 순회의 경우 가장 마지막- 이진 트리가 아닌 일반적인 트리에도 사용 가능한 순회인 반면 중위 순회의 경우 본인을 언제 방문할 것인지 결정되지 않기 때문에 이진 트리가 아닌 트리에서는 사용하기 모호하다.

##### 전위 순회(Preorder Traversal)

수행 방법 및 순서는 아래와 같다.

1. 현재 노드 N을 방문하여 처리한다.
2. 현재 노드 N의 왼쪽 서브 트리로 이동한다.
3. 현재 노드 N의 오른쪽 서브 트리로 이동한다.

이를 구현하면 아래와 같다.

```Python
def preorder_traversal(visit: list[int], dp: list[bool], node: 'Node'):
    if node and not dp[node.index]:
        visit.append(node.value)
        dp[node.index] = True
        preorder_traversal(visit=visit, dp=dp, node=node.left)
        preorder_traversal(visit=visit, dp=dp, node=node.right)

    else:
        return None
```

전위 순회에 따른 방문 값을 저장한 리스트 변수 `visit` 을 출력하면 `[None, 1, 2, 4, 5, 3, 6, 7]` 와 같다.

이를 활용하여 수식에 대한 전위 표기식을 구할 수 있다.

##### 중위 순회(Inorder Traversal)

수행 방법 및 순서는 아래와 같다.

1. 현재 노드 N의 왼쪽 서브 트리로 이동한다.
2. 현재 노드 N을 방문하여 처리한다.
3. 현재 노드 N의 오른쪽 서브 트리로 이동한다.

이를 구현하면 아래와 같다.

```Python
def inorder_traversal(visit: list[int], dp: list[bool], node: 'Node'):
    if node and not dp[node.index]:
        inorder_traversal(visit=visit, dp=dp, node=node.left)
        dp[node.index] = True
        visit.append(node.value)
        inorder_traversal(visit=visit, dp=dp, node=node.right)

    else:
        return None
```

중위 순회에 따른 방문 값을 저장한 리스트 변수 `visit` 을 출력하면 `[None, 4, 2, 5, 1, 6, 3, 7]` 와 같다.

이를 활용하여 수식에 대한 중위 표기식을 구할 수 있다.

##### 후위 순회(Postorder Traversal)

수행 방법 및 순서는 아래와 같다.

1. 현재 노드 N의 왼쪽 서브 트리로 이동한다.
2. 현재 노드 N의 오른쪽 서브 트리로 이동한다.
3. 현재 노드 N을 방문하여 처리한다.

이를 구현하면 아래와 같다.

```Python
def postorder_traversal(visit: list[int], dp: list[bool], node: 'Node'):
    if node and not dp[node.index]:
        postorder_traversal(visit=visit, dp=dp, node=node.left)
        postorder_traversal(visit=visit, dp=dp, node=node.right)
        dp[node.index] = True
        visit.append(node.value)

    else:
        return None
```

후위 순회에 따른 방문 값을 저장한 리스트 변수 `visit` 을 출력하면 `[None, 4, 5, 2, 6, 7, 3, 1]` 와 같다.

이를 활용하여 수식에 대한 후위 표기식을 구할 수 있다.

#### 트리 순회의 응용

##### 전위 순회

트리 구조로 저장된 교과서 목차(Index)를 출력할 때 전위 순회를 사용할 수 있다.

##### 중위 순회

트리 구조를 이용하여 수식 연산을 표기할 때 중위 순회를 사용할 수 있다.

##### 후위 순회

트리 구조를 이용하여 디렉토리의 용량을 계산할 때 이용할 수 있다.

#### 이진 탐색 트리

##### 정의

이진 탐색 트리, 일명 BST(Binary Search Tree)는 이진 트리에 탐색을 위한 조건을 추가하여 정의한 자료 구조를 의미한다.

##### 조건

이진 탐색 트리가 되기 위해서는 아래와 같은 조건을 충족해야 한다.

1. 모든 원소는 서로 다른 유일한 키를 갖는다.
2. 왼쪽 서브 트리에 있는 원소의 키들은 그 루트의 키보다 작다.
3. 오른쪽 서브 트리에 있는 원소의 키들은 그 루트의 키보다 크다.
4. 왼쪽 서브 트리와 오른쪽 서브 트리도 이진 탐색 트리다.

##### 주의점

루트 노드를 기준으로 왼쪽 자식 노드와 오른쪽 자식 노드의 깊이가 일정한 균형 잡인 트리 -일명 AVL(Adelson-Velskii Lendis) 트리- 인 경우가 가장 좋다.

예를 들어 루트 노드가 노드의 값들 중 가장 큰 값인 경우 좌측 편향 트리가 만들어지기 때문에 이진 탐색 트리의 탐색 속도 효율성을 장점으로 가져갈 수 없어 비효율적이다.

만약 편향된 트리가 될 경우 트리를 다시 수정해서 중간값을 루트 노드의 값으로 변경하는 방법도 있다.

### 실습

#### 문제

수식 `A*B - C/D`에 대한 이진 트리를 생성하고 전위 순회, 중위 순회, 후위 순회를 차례로 수행하면서 순회경로를 출력하는 메서드를 작성하시오.

#### 코드

```Python
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
```
