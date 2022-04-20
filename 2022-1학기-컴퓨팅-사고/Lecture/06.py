"""
6주차: 조건문
- 코드 블록
- `if`, `elif`, `else`
- 중첩 조건문
"""

if __name__ == "__main__":
    from datetime import datetime
    
    day_num: int = datetime.today().day
    car_num: int = int(input("차량 번호 4자리를 입력하세요. "))
    
    print(f"오늘 날짜: {day_num}일")
    if enter_car_day := (day_num % 2):
        print("오늘 입차: 번호가 홀수인 차량")
    else:
        print("오늘 입차: 번호가 짝수인 차량")
        
    if enter_car_day == (car_num % 2):
        print("귀하의 차량은 입차 가능합니다.")
    else:
        print("귀하의 차량은 입차 불가합니다.")
        
    
    life_time: int = int(input("최초 장비를 사용하기까지 걸린 시간(초)를 입력하세요. "))
    
    if life_time <= 60:
        print("생존율: 85%")
    elif life_time <= 120:
        print("생존율: 76%")
    elif life_time <= 180:
        print("생존율: 66%")
    elif life_time <= 240:
        print("생존율: 57%") 
    elif life_time <= 300:
        print("생존율: 47%")
    elif life_time <= 360:
        print("생존율: 37%")
    else:
        print("생존율: 25% 미만")
        
    
    amount: float = float(input("전기 사용량을 입력하세요. "))
    
    if amount > 400:
        basic_price = 7300
        unit_price = 280.6
    elif amount > 201:
        basic_price = 1600
        unit_price = 187.9
    else:
        basic_price = 910
        unit_price = 99.3
        
    total_price = (amount * unit_price) + basic_price
    print(f"사용량: {amount}kwh")
    print(f"기본요금: {basic_price}원")
    print(f"단가: {unit_price}원")
    print(f"전기 요금: {total_price}원")
        