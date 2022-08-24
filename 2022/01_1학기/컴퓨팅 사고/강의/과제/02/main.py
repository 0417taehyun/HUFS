"""
코드 설명

수학시험프로그램과 회원가입프로그램의 코드에 대한 설명을 주석으로 작성하여 제출
"""

if __name__ == "__main__":
    """
    수학시험프로그램
    """
    # 문제, 정답, 배점 순서로 아이템이 저장되어 있는 리스트가 들어있는 튜플 정의
    quiz: tuple[list] = (
        ["3+2", 5, 3], ["5/2의 몫", 2, 5], ["10-2", 8, 3],
        ["10^2*2", 200, 5], ["1-(10/4의 나머지)", -1, 5],
        ["2^4", 16, 3], ["4/2", 2, 3]
    )

    answer_count: int = 0 # 정답의 개수를 셀 변수
    wrong_answer_count: int = 0 # 오답의 개수를 셀 변수
    total_score: int = 0 # 정답 문제의 배점이 합산될 변수
     
    for item in quiz: # 튜플의 리스틀 for 반복문을 통해 하나씩 조회
        print("문제 : ", item[0]) # 리스트의 첫 번째 아이템인 문제를 출력
        answer: int = int(input("정답을 입력하세요. ")) # 사용자로부터 input 함수를 통해 정답을 입력 받음
        
        if answer == item[1]: # 리스트의 두 번째 아이템인 문제의 정답과 사용자의 입력 값이 같은 경우
            answer_count += 1 # 정답의 개수를 셀 변수인 answer_count 변수의 값을 하나 상승
            total_score += item[2] # 리스트의 세 번째 아이템인 배점을 total_score 변수에 합산
        
        else: # 만약 문제의 정답과 사용자의 입력 값이 다른 경우
            wrong_answer_count += 1 # 오답의 개수를 셀 변수인 wrong_answer_count 변수의 값을 하나 상승
    
    print('-' * 30) # 출력을 꾸며주기 위해 문자 '-'를 30회 출력
    print("정답 개수\t: ", answer_count) # answer_count 변수를 활용하여 정답 개수 출력
    print("오답 개수\t: ", wrong_answer_count) # wrong_answer_count 변수를 활용하여 오답 개수 출력
    print("Total Score\t: ", total_score) # total_score 변수를 활용하여 총 배점 출력
    print('-' * 30) # 출력을 꾸며주기 위해 문자 '-'를 30회 출력
    
    
    """
    회원가입 프로그램
    """
    members: dict[str, str] = {} # 문자열인 id 변수를 키로, 문자열인 pw 변수를 값으로 저장하기 위한 딕셔너리 변수
    flag: bool = True # while 문의 반복여부를 위한 변수 flag
    
    while flag: # flag 변수의 값을 False로 바꾸지 않는 이상 무한루프
        select_num: int = int(input("\n1.회원가입, 2.프로그램종료\t")) # 사용자로부터 input 함수를 통해 두 가지 행동 중 하나를 입력 받음
        
        if select_num == 1: # 사용자가 회원가입을 선택한 경우
            id: str = input("아이디를 입력하세요.\t") # 사용자로부터 input 함수를 통해 문자열인 id 변수 값을 입력 받음
            pw: str = input("비밀번호를 입력하세요.\t") # 사용자로부터 input 함수를 통해 문자열인 pw 변수 값을 입력 받음
            members[id] = pw
        
        elif select_num == 2: # 사용자가 프로그램종료를 선택한 경우
            print('-' * 30) # 출력을 꾸며주기 위해 문자 '-'를 30회 출력
            print('아이디 : 비밀번호') # 아래 값들이 아이디 : 비밀번호 모양으로 출력이 될 것을 알려주는 출력
            print('-' * 30) # 출력을 꾸며주기 위해 문자 '-'를 30회 출력
            
            for key in members.keys(): # key() 메서드를 통해 members 딕셔너리 변수의 전체 키 값을 조회하고 이를 for 반복문을 통해 하나씩 조회
                print(key, "\t:\t", members[key]) # members 변수의 키를 먼저 출력하고 이후 해당 키를 통해 알맞는 members 변수의 값을 출력
                
            print('-' * 30) # 출력을 꾸며주기 위해 문자 '-'를 30회 출력

            flag = False # 무한루프를 돌고 있는 while 문을 빠져나오기 위해 flag 변수의 값을 False로 재할당
            