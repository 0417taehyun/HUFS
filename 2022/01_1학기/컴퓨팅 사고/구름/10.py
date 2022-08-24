"""
10주차: 리스트 다루기
- 리스트 수정과 삭제
- 리스트 함수
"""

if __name__ == "__main__":
    answers: str = input()

    total: int = 0
    current: int = 1

    for answer in answers:
        if answer == 'O':
            total += current
            current += 1
        elif answer == 'X':
            if current != 1:
                current = 1
        
    print(total)