"""
14주차: 파일 입출력
- 파일 생성과 작성
- 파일 읽기와 내용 추가
"""

if __name__ == "__main__":
    f = open("data/about_python.txt", "r")
    sentences: list[str] = []
    idx: int = 0
    
    while True:
        data: str = f.readline()
        
        if not data:
            break
        else:
            numbering = f"{idx+1}번 문장 "
            data = numbering + data
            sentences.append(data)
            idx += 1
    f.close()            

    f = open("data/about_python.txt", "w")
    
    for sentence in sentences:
        f.write(sentence)
    f.close()
        
    f = open("data/about_python.txt", "r")
    print(f.read())
    f.close()