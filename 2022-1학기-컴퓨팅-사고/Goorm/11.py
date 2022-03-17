"""
11주차: 또 다른 묶음 자료형
- 사전 자료형
- 튜플 자료형
- 집합 자료형
"""

if __name__ == "__main__":
    d: dict[str, int] = {
        "pencil": 500,
        "eraser": 700,
        "notebook": 1500,
        "eraser": 700,
        "scissors": 3000,
        "tape": 2700,
        "pencil": 500,
        "pencil": 500,
        "notebook": 1500,
        "tape": 2700
    }

    d["white"] = 1900
    print(d["white"])

    print(len(d.keys()))