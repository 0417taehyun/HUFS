"""
13주차: 함수 파헤치기
- 매개변수
- 반환값
- 전역변수와 지역변수
"""

if __name__ == "__main__":
    invest_money: int = int(input("투자 액수를 입력하세요: "))
    invest_date: int = int(input("투자한 날짜 수를 입력하세요: "))
    invest_result: int = invest_money

    def calc(invest_result: int, invest_date: int) -> None:
        for date in range(1, invest_date + 1):
            changed_percentage: int = int(input(f"{date}일차 변동 데이터를 입력하세요: "))
            invest_result *= (100 + changed_percentage) / 100
        
        result = int(invest_result - invest_money)
        
        print(result)
        
        if result > 0:
            print("이득입니다.")
        elif result == 0:
            print("본전입니다.")
        else:
            print("손해입니다.")
    
    calc(invest_result=invest_money, invest_date=invest_date)