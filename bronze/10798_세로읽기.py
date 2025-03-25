arr = [input() for _ in range(5)]

for c in range(15): # 열 15개 순회
    for r in range(5):  # 행 5개 순회
        if c < len(arr[r]): # 현재 줄에 글자가 존재하는 동안만 출력
            print(arr[r][c], end='')