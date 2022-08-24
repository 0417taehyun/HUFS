"""
12주차: 함수의 기초
- 함수의 구성과 사용
"""

if __name__ == "__main__":
    def average(kor: int, eng: int, math: int) -> int:
        return (kor + eng + math) / 3
            
    kor: int = int(input("국어 점수를 입력하세요: "))
    eng: int = int(input("영어 점수를 입력하세요: "))
    math: int = int(input("수학 점수를 입력하세요: "))

    print(f"국어는 {kor}점, 영어는 {eng}점, 수학은 {math}점이며, 총 평균은 {average(kor, eng, math):.2f}점입니다.")