"""
2주차: 파이썬 시작하기
- 콘솔 입출력
- 변수
"""

if __name__ == "__main__":
    print("간단한 설문조사를 진행하겠습니다.")
    
    name: str = input("1. 당신의 이름은 무엇인가요?")
    number: int = int(input("2. 당신의 학번은 무엇인가요?"))
    major: str = input("3. 당신의 전공은 무엇인가요?")
    place: str = input("4. 입학 후 학교에서 가장 먼저 방문한 곳은 어디인가요?")
    event: str = input("5. 학교생활 중 가장 기대하는 것은 무엇인가요?")
    
    print()
    print("====")
    print(name, "님 안녕하세요.")
    print(f"{name} 님의 전공은 {major} 이며, 학번은 {number} 입니다.")
    print(f"{name} 님은 한국외국어대학교에서 {place} 에 가장 먼저 방문하셨습니다.")
    print(f"{event} 을(를) 가장 기대하는 {name} 님의 학교 생활을 응원합니다.")
    print("====")