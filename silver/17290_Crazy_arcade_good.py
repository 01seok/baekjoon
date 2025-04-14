r, c = map(int, input().split())    # 플레이어 위치
field = [list(input()) for _ in range(10)]

r -= 1  # 1번부터 시작하니까 인덱스 번호 맞춰주기
c -= 1

bomb_row = set()    # 폭탄 있는 행 번호 담기
bomb_col = set()    # 폭탄 있는 열 번호 담기
for i in range(10):
    for j in range(10):
        if field[i][j] == 'o':
            bomb_row.add(i)
            bomb_col.add(j)

min_move = 100
for i in range(10):
    if i in bomb_row:   # 폭탄 있는 행 패스
        continue
    for j in range(10):
        if j in bomb_col:   # 폭탄 있는 열 패스
            continue
        distance = abs(r - i) + abs(c - j)  # 안전지대들과 현재 있는 곳 맨해튼 거리 구하기
        min_move = min(min_move, distance)  # 최소 값 갱신
print(min_move)
