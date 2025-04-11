paper = [[0] * 1001 for _ in range(1001)]   # 최대 가로 세로 1001 x 1001
N = int(input())    # 색종이 개수

for num in range(1, N + 1):
    x, y, w, h = map(int, input().split())  # 왼쪽 아래 모서리 x,y 좌표, w:너비, h:높이

    for r in range(y, y + h):   # 행은 주어진 y좌표부터 높이 h만큼
        for c in range(x, x + w):   # 열은 주어진 x좌표부터 너비 w만큼
            paper[r][c] = num       # 자기 번호로 채우기

for num in range(1, N + 1):
    cnt = 0
    for r in range(1001):
        for c in range(1001):
            if paper[r][c] == num:  # 자기 순서의 숫자와 (num의 숫자) 같다면 보이는 영역
                cnt += 1    # 보이는 영역 1 추가

    print(cnt)
