if __name__ == "__main__":
    """
    문자를 하나씩 입력 받아 리스트에 저장한 후, 스택 연산을 활용하여 입력 받은 문자의 역순 문자열을 생성하여 출력하는 프로그램을 작성하시오.
    
    - 문자가 아닌 다른 값(숫자 등이)이 입력될 때까지 입력을 계속 받는다.
    - 최종 출력 결과에서 리스트는 empty 상태가 되어야 한다.
    """
    import re
    
    
    stack: list[str] = []
    while re.match(
        r"[a-zA-Z]",
        (character := input("Input character: "))
    ):
        stack.append(character)
    
    answer: str = ""
    print(f"1 >>> {stack}")
    for _ in range(len(stack)):
        answer += stack.pop()
    
    print(f"2 >>> {stack}")
    print(f"3 >>> {answer}")
    