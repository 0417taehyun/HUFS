# Python의 클래스와 리스트를 활용한 스택(Stack) 구현

class Stack:
    """
    아래와 같이 멤버 변수(Member Variable) -인스턴스 변수(Instacne Variable)라고도 함- 가 아닌
    클래스 변수(Class Variable)로 stack_size 변수를 정의해줄 수도 있다.
    이 경우 생성된 모든 스택 객체가 동일한 스택 사이즈를 공유한다는 걸 가정한다.
    
    stack_size: int = 3
    """
    def __init__(self, size: int) -> None:
        self.limit_size: int = size
        self.current_size: int = 0
        self.stack: list[int] = []

    def __call__(self) -> None:
        print(self.stack)

    def push(self, value: int) -> None:
        if self.current_size == self.limit_size:
            print("Stack is full!")
            
        else:
            self.current_size += 1
            self.stack.append(value)
            print(f"{value} inserted")

    def pop(self) -> None:
        if self.current_size == 0:
            print("Stack is empty!")
            
        else:
            self.current_size -= 1
            top: int = self.stack.pop()
            print(f"{top} deleted")


if __name__ == "__main__":
    size: int = 3
    
    stack = Stack(size)

    for number in range(1, size+1):
        stack.push(number)
        
    stack()
    stack.push(size+1)

    for _ in range(1, size+1):
        stack.pop()

    stack()
    stack.pop()
