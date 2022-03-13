"""
15주차: 모듈
- 모듈 기본 이론 및 실습
"""

if __name__ == "__main__":
    movies: list[str] = ["Dark Knight", "Harry Porter", "Parasite", "Matrix", "La La Land"]

    print()
    print("===========영화 목록===========")
    for movie in movies:
        print(movie)
    print("==============================")
        
    choice: str = input("예매하실 영화를 선택해주세요: ")

    while choice not in movies:
        print("예매할 수 없는 영화입니다")
        choice: str = input("예매하실 영화를 선택해주세요: ")

    print(f"{choice}를 선택하셨습니다")
        
    check: bool = False

    while(not(check)):

        people: int = int(input("관람 인원 수를 입력해주세요: "))
        if people <= 0:
            print("관람 인원 수는 양수만 가능합니다")		
        else:
            break
    print("관람할 인원 수는 %d명입니다" %people)
        
    coupon_dic: dict[str, int] = {'WELCOME':2000, 'VALENTINE':3000, 'CHRISTMAS':4000, 'INDEPENDENCE':5000}
    process: bool = True

    usage: str = input("할인권을 사용하시려면 y, 금액 확인으로 넘어가시려면 n을 입력해주세요: ")

    while process:
        if usage == 'y':
            coupon: str = input("쿠폰 번호를 입력해주세요: ")
            if coupon in coupon_dic.keys():
                sale = coupon_dic[coupon]
                print("%d원 할인됩니다" %sale)
                break
            else:
                print('존재하지 않는 할인권입니다')
                usage: str = input("할인권을 다시 입력하려면 y, 아니면 n을 입력해주세요: ")
        elif usage == 'n':
            sale = 0
            print('할인권을 사용하지 않았습니다')
            break
        else:
            usage = input('잘못된 입력입니다. 다시 입력해주세요: ')

    origin_price: int = 12000 * people
    sale_price: int = sale * people
    total_price: int = origin_price - sale_price

    print("")
    print("<예매 상세 내역>")
    print("==============================")
    print(f"영화 제목: {choice}")
    print(f"관람 인원: {people}명")
    print(f"합산 금액: {origin_price}원")
    print(f"할인 금액: {sale_price}원")
    print("------------------------------")
    print(f"실 결제액: {total_price}원")
    print("==============================")