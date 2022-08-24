"""
MP3 플레이어 함수

과제의 조건은 아래와 같다.
아래의 각 기능을 함수로 만들어야 한다.
1. 곡 추가
2. 곡 제거
3. 곡 리스트 출력
4. 일반 재생 모드
5. 셔플 재생 모드
"""

if __name__ == "__main__":
    from random import sample
    
    
    playlist: list[str] = [
        "Dynamite.mp3", "다시 여기 바닷가.mp3", "마리아 (Maria).mp3",
        "When We Disco.mp3", "How You Like That.mp3", "눈누난나.mp3",
        "그 여름을 틀어줘.mp3"
    ]
    
    
    def add_music(playlist: list[str] = playlist) -> None:
        """
        곡 추가 함수
        """
        music: str = input("추가할 곡을 입력하세요: ")
        playlist.append(music)
    
    
    def remove_music(playlist: list[str] = playlist) -> None:
        """
        곡 제거 함수
        """
        music: str = input("삭제할 곡을 입력하세요: ")
        playlist.remove(music)
    
    
    def get_music_list(playlist: list[str] = playlist) -> None:
        """
        곡 리스트 출력 함수
        """
        print("플레이리스트 목록을 보여줍니다.")
        print('-' * 51)
        for music in playlist:
            print(music)
    
    
    def play_music(playlist: list[str] = playlist) -> None:
        """
        일반 재생 모드 함수
        """
        print("음악이 추가된 아래의 순서로 재생됩니다.")
        print('-' * 51)
        for music in playlist:
            print(music)
    
    
    def play_music_shuffle(playlist: list[str] = playlist) -> None:
        """
        셔플 재생 모드 함수
        """
        playlist = sample(playlist, len(playlist))
        print("음악이 셔플되어 아래의 순서로 재생됩니다.")
        print('-' * 51)
        for music in playlist:
            print(music)
    

    while True:  
        print('-' * 51)
        print("1. 곡 추가\n2. 곡 제거\n3. 곡 리스트 출력\n4. 일반 재생 모드\n5. 셔플 재생 모드\n6. 종료")
        print('-' * 51)
        function_selection: str = input("위 다섯 가지 기능 중 원하는 기능의 번호를 입력하세요. ")
        
        if function_selection == '1':
            add_music()
            
        elif function_selection == '2':
            remove_music()
            
        elif function_selection == '3':
            get_music_list()
            
        elif function_selection == '4':
            play_music()
            
        elif function_selection == '5':
            play_music_shuffle()
  
        elif function_selection == '6':
            print('-' * 51)
            print("MP3 플레이어를 종료합니다.")
            break
        
        else:
            continue
