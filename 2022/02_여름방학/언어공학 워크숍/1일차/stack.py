# Python의 클래스와 리스트를 활용한 스택(Stack) 구현

class Stack:
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
    stack = Stack(3)

    for number in range(1, 4):
        stack.push(number)
        
    stack()
    stack.push(4)

    for _ in range(1, 4):
        stack.pop()

    stack()
    stack.pop()
    