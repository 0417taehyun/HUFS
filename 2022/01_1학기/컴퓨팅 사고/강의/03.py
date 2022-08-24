"""
3주차: 파이썬 첫걸음
- 출력(`print`)
- 컴파일러와 인터프리터
- 터틀 프로그래밍
"""

if __name__ == "__main__":
    print("친구야~ 안녕~~.")
    print("선배님 안녕하세요.")
    print("교수님 안녕하세요.")
    
    
    import turtle
    
    t = turtle.Turtle()
    t.shape("turtle")
    
    # 직사각형
    t.forward(100)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(150)
    
    # 정삼각형
    t.right(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
    
    # 원
    t.circle(50)
    