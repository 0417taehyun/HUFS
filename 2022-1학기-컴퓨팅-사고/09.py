"""
9주차: 리스트 시작하기
- 메모리
- 인덱싱과 슬라이싱
"""

if __name__ == "__main__":
    num_list = []
    sum = 0
    
    while True:
        num: int = int(input("몇 개를 입력하시겠습니까? "))

        if num < 0:
            print("다시 입력하세요")
        else:
            break
        
    for _ in range(num):
        data: int = int(input("넣을 숫자를 입력하세요: "))
        num_list.append(data)
        sum += data
        
    print(num_list)
    print('총합: %d' %sum)