"""
4주차: 데이터와 변수
- 데이터와 변수
- 자료형의 종류와 형변환
"""

if __name__ == "__main__":
    print("회원 정보를 입력하세요. ")
    user_name: str = input("이름: ")
    user_email: str = input("이메일: ")
    user_id: str = input("아이디: ")
    user_password: str = input("비밀번호: ")
    
    print("-" * 30)
    print(f"To. {user_email}")
    print("> 아이디 및 비밀번호 확인")
    print(f"{user_name} 고객님 안녕하세요.")
    print(f"{user_name} 고객님의 아이디와 비밀번호는 아래와 같습니다.")
    print(f"아이디: {user_id}")
    print(f"비밀번호: {user_password}")
    print("-" * 30)
    
    
    print()
    print()
    
    print("내일 날씨 정보를 입력하세요.")
    day: str = input("요일: ")
    date: str = input("날짜: ")
    lowest_temperature: str = input("아침 최저기온: ")
    highest_temperature: str = input("낮 최고기온: ")
    raining_percentage: str = input("비올 확률: ")
    fine_dust_status: str = input("미세먼지: ")
    sunrise_time: str = input("일출 시간: ")
    sunset_time: str = input("일몰 시간: ")
    south_ocean_wave: str = input("남해 물결 높이: ")
    east_ocean_wave: str = input("동해 물결 높이: ")
    west_ocean_wave: str = input("서해 물결 높이: ")
    
    print("내일 날씨 예보입니다.")
    print(f"{day}요일인 {date}의 아침 최저 기온은 {lowest_temperature}도, 낮 최고 기온은 {highest_temperature}도로 예보됐습니다.")
    print(f"비올 확률은 {raining_percentage}%이고, 미세먼지는 {fine_dust_status} 수준일 것으로 예상됩니다.")
    print(f"일출 시간은 {sunrise_time}이고, 일몰 시간은 {sunset_time}입니다.")
    print(f"바다의 물결은 남해 앞바다 {south_ocean_wave}m, 동해 앞바다 {east_ocean_wave}m, 서해 앞바다 {west_ocean_wave}m 높이로 일겠습니다.")
    print(f"지금까지 {date} {day}요일 날씨 예보였습니다.")
    
    