"""
6주차: 반복문
- `for` 및 `while` 반복문
"""

if __name__ == "__main__":
    start_day = 2
    last_day = 31

    print('\tS\tM\tT\tW\tT\tF\tS')
    for _ in range(start_day):
        print('\t', end='')
    for i in range(1, last_day+1):
        if (i + start_day) % 7:
            print('\t%d' %i, end='')
        elif (i + start_day) % 7 == 0:
            print('\t%d\n' %i)