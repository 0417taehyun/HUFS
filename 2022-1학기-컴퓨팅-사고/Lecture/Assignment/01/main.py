"""
난수 맞히기 게임

과제의 조건은 아래와 같다.
1. 0부터 100까지의 난수를 발생시킨다.
2. 사용자가 입력한 숫자가 난수와 일치하면 '정답입니다'를 출력하고 게임을 종료한다
3. 사용자가 입력한 숫자가 난수와 일치하지 않으면 틀렸습니다. 다시입력하세요' 출력하고 다시 물어본다.
4. 사용자가 틀릴때마다 사용자가 입력한 숫자와 난수를 비교하여 크고 작음을 출력한다.
5. 기회는 10회로 제한한다. 만약 10번을 넘어가면 '게임에 졌습니다'를 출력하고 게임을 종료한다.
6. 게임이 종료하기 전 난수를 출력한다.
"""

if __name__ == "__main__":    
    from random import randint
    answer: int = randint(0, 100)
    count: int = 0
    
    print("숫자 게임을 시작합니다. 총 기회는 10번이니 힌트를 기반으로 신중하게 입력해주세요!")
    print("-" * 81)
    
    user_input: int = int(input("0부터 100까지의 정수 중 하나를 입력해주세요: "))
                                
    while True:
        count += 1
        
        if count == 10:
            print("기회 10번을 모두 사용하셨습니다. 게임에 졌습니다.")
            break
        
        if (user_input == answer):
            print(f"{count}번만에 맞추셨네요! 정답입니다. ")
            break
        else:
            print("틀렸습니다. ", end='')
            
            if user_input > answer:
                print(f"입력하신 수 {user_input}보다 작습니다. ", end='')
            else:
                print(f"입력하신 수 {user_input}보다 큽니다. ", end='')
                
            user_input = int(input("다시 입력하세요: "))
    
    print("-" * 81)
    print(f"숫자는 {answer}이었습니다.")
    