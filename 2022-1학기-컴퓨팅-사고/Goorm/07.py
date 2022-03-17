"""
7주차: 조건문과 반복문 활용
- 중첩 반복문
- 제어문
"""

if __name__ == "__main__":
    while True:
        print("1. 더하기")
        print("2. 빼기")
        print("3. 곱하기")
        print("4. 나누기")
        print("5. 프로그램 종료")
        menu = int(input("원하는 기능의 번호를 입력하세요: "))
        
        if menu == 5:
            print("프로그램을 종료합니다.")
            break
        
        elif (menu == 1) or (menu == 2) or (menu == 3) or (menu == 4):
            first_num: int = int(input("첫 번째 정수를 입력하세요: "))
            second_num: int = int(input("두 번째 정수를 입력하세요: "))
            
            if menu == 1:
                print(f"{first_num}와 {second_num}를 더하기 연산한 결과는 {first_num+second_num}입니다.")
            
            elif menu == 2:
                print(f"{first_num}에서 {second_num}를 빼기 연산한 결과는 {first_num-second_num}입니다.")
            
            elif menu == 3:
                print(f"{first_num}와 {second_num}를 곱하기 연산한 결과는 {first_num*second_num}입니다.")
            
            else:
                if not second_num:
                    print("연산이 불가합니다.")
                else:
                    print("%d를 %d로 나누기 연산한 결과는 %f입니다." %(first_num, second_num, first_num/second_num))
        
        else:
            print("잘못된 번호입니다.")