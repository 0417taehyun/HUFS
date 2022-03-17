"""
5주차: 논리 요소와 조건문
- `bool` 자료형
- 논리연산자와 관계연산자
- 조건문
"""

if __name__ == "__main__":
    year: int = int(input("연도를 입력하세요."))
    
    if ((not (year % 4)) and (year % 100)) or (not (year % 400)):
        print(f"{year}년은 윤년입니다.")
    else:
        print(f"{year}년은 윤년이 아닙니다.")