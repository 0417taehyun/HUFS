"""
5주차: 연산자
- 산술, 할당, 비교, 논리 연산자
- `operator` 모듈
"""

if __name__ == "__main__":
    """
    operator 모듈을 사용할 경우 연산자 기호를 사용하는 것보다 연산 속도가 빠르다.
    연산 기호를 사용하는 경우 파이썬 내부적으로 기호를 함수로 변환해서 연산을 실행하게 되는데,
    operator 모듈의 함수를 사용하면 기호를 함수로 변환하는 과정이 생략되기 때문이다.
    """
    import operator
    
    TEMPERATURE_OF_SEA_LEVEL: int = 20
    data: int = int(input("수심을 입력하세요. "))
    temperature: float = operator.sub(
        TEMPERATURE_OF_SEA_LEVEL, operator.mul(
            operator.floordiv(data, 10), 0.7
        )
    )
    print(f"수온: {temperature}")
    
    
    speed: int = int(input("주행 속도: "))
    time: int = int(input("주행 시간: "))
    distance: int = operator.mul(speed, time)
    print("주행 이동 거리: ", distance)
    
    
    time: int = int(input("근무시간을 입력하세요. "))
    computer: int = operator.floordiv(operator.mul(3, 8), time)
    add_computer: bool = True if operator.mod(operator.mul(3, 8), time) > 0 else False
    print(f"필요한 컴퓨터: {computer + add_computer}")