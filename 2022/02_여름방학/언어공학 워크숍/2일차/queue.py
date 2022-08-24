# Python의 클래스와 리스트를 활용한 큐(Queue) 구현

class Queue:
    queue_size: int = 3
    
    def __init__(self) -> None:
        self.current_size: int = 0
        self.queue: list[int] = []
        
    def __call__(self) -> None:
        print(self.queue)
    
    def enqueue(self, value: int) -> None:
        if self.current_size == Queue.queue_size:
            print("Queue is full!")
            
        else:
            self.current_size += 1
            self.queue.append(value)
            print(f"{value} inserted")
    
    def dequeue(self) -> None:
        if self.current_size == 0:
            print("Queue is empty!")
            
        else:
            self.current_size -= 1
            element: int = self.queue.pop(0)
            print(f"{element} deleted")


if __name__ == "__main__":
    queue: Queue = Queue()
    for value in range(1, 4):
        queue.enqueue(value=value)
    
    queue()
    queue.enqueue(4)
    
    for _ in range(3):
        queue.dequeue()
    
    queue()
    queue.dequeue()
    