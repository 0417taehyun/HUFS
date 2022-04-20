"""
7주차: 반복문
- `for`
- `range()`
- `while`
- 무한 루프
- 반복문 내 실행 제어
- 중첩 반복문
"""

if __name__ == "__main__":
    for num in range(1, 100):
        if num <= 9:
            if num % 3:
                print(num, end='')
            else:
                print(f"{num} 짝!", end='')
        
        else:
            print(num, end='')
              
            if not ((num // 10) % 3):
                print(" 짝!", end='')
            if not (num % 10) % 3 and (num % 10) != 0:
                print(" 짝!", end='')
        
        print()
        
        
    train_a, train_b, train_c = 10, 25, 30
    
    for num in range(1, 541):
        if not ((num % train_a) and (num % train_b)):
            print(f"{9 + (num // 60)}시 {num % 60}분")
        elif not ((num % train_b) and (num % train_c)):
            print(f"{9 + (num // 60)}시 {num % 60}분")
        elif not ((num % train_c) and (num % train_a)):
            print(f"{9 + (num // 60)}시 {num % 60}분")
            
            
    admin_password: str = "hanbitac"
    count: int = 1
    
    while True:
        if count > 5:
            print("로그인 실패!! 횟수 초과!!!")
            break
        
        input_password = input("관리자 암호를 입력하세요. ")
        
        if input_password != admin_password:
            print("암호를 다시 확인하세요!")
            count += 1
        
        elif input_password == admin_password:
            print("로그인 됐습니다.")
            break
        