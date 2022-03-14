"""
1주차: 파이썬 클래스 단계별 복습
- `__future__` 모듈
- 매직 메서드와 오버로딩
- 멤버 변수 및 Non-Public 변수
- 이터레이터
"""

from __future__ import annotations

if __name__ == "__main__":
    class Point:
        def __init__(self, x: int = 0, y: int = 0) -> None:
            self.x: int = x
            self.y: int = y
        
        """
        파이썬 클래스 메서드의 종류에는 크게 일반 메서드와 매직 메서드가 존재한다.
        이때 메직 메서드의 경우 관례적으로 언더스코어(__)를 앞뒤에 붙여준다.
        """
        def __str__(self) -> str:
            return f"({self.x}, {self.y})"
        
        def __add__(self, other: Point) -> Point:
            return Point(self.x + other.x, self.y + other.y)
        
        def __sub__(self, other: Point) -> Point:
            return Point(self.x - other.x, self.y - other.y)
        
        def __rmul__(self, other: int) -> Point:
            """
            매직 메서드 __rmul__의 경우 우측에 등장하는 객체가 self가 된다.
            """
            return Point(self.x * other, self.y * other)
        
        def length(self) -> float:
            from math import sqrt
            return sqrt(self.x**2 + self.y**2)
    
        def dot(self, q: Point) -> int:
            return (self.x * q.x) + (self.y * q.y)
        
        def dist(self, q: Point) -> float:
            return (self - q).length()
        
        def move(self, dx: int = 0, dy: int = 0) -> None:
            self.x += dx
            self.y += dy
            
        def get_x(self) -> int:
            return self.x
        
        def get_y(self) -> int:
            return self.y
        
        def get(self) -> tuple:
            return (self.x, self.y)
        
        def set_x(self, value: int) -> None:
            self.x = value
        
        def set_y(self, value: int) -> None:
            self.y = value
        
        def set(self, *args: tuple(int)) -> None:
            self.x, self.y = args[0], args[1]
    
    
    point = Point(1, 2)
    print("Point: ", point)
    print("__str__: ", str(point))

    other = Point(3,4)
    print("Other: ", other)
    
    """
    __add__, __sub__ 등의 사칙연산 관련 메직 메서드의 경우 아래와 같이 연산자를 통해 실행할 수 있다.
    이처럼 연산자에 클래스의 메서드를 덧입혔다는 의미로 오버로딩(Overloading)이라 부른다.
    """
    print("__add__: ", point + other)
    print("__sub__: ", point - other)
    print("__rmul__: ", 3 * point)
    
    print("length: ", point.length())
    print("dot: ", point.dot(other))
    print("dist: ", point.dist(other))
    point.move(dx=7, dy=2)
    print("move: ", point)
    
    print("get_x: ", point.get_x())
    print("get_y: ", point.get_y())
    print("get: ", point.get())
    
    point.set_x(10)
    print("After set_x: ", point.get_x())
    point.set_y(20)
    print("After set_y: ", point.get_y())
    point.set(50, 50)
    print("After set: ", point.get())
    
    class Vector:
        def __init__(self, *args: tuple(int)) -> None:
            """
            언더바(_)로 시작하는 멤버 변수는 Non-Public 변수라 부른다.
            다른 곳에서 이 클래스를 `import`하여 사용하더라도 해당 멤버 변수는 감춰진다.
            이를 참조하기 위해서는 아래에서 만드는 매직 메서드 __getitem__ 및 __setitem__을 사용해야 한다.
            """
            self._coords: list = list(args)
            
        def __str__(self) -> str:
            return str(tuple(self._coords))
        
        """
        __len__ 및 __getitem__ 메서드가 정의되면 해당 클레스에 대한 이터레이터(Iterator)가 자동으로 정의된다.
        물론 이외에도 __iter__ 메서드를 정의하거나 `yield`를 사용한 제너레이터(Generator)를 정의하는 방법도 존재한다.
        """
        def __len__(self) -> int:
            return len(self._coords)
        
        def __getitem__(self, index: int) -> int:
            return self._coords[index]
        
        def __setitem__(self, index: int, value: int) -> None:
            self._coords[index] = value
            
            
    vector = Vector(1, 2, 3)
    print("Vector: ", vector)
    
    vector[-1] = 9
    print("After __setitem__ on index -1: ", vector[-1])
    for item in vector:
        print("item in Vector: ", item)
    
    