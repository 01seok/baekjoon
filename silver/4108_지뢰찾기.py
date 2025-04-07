dr = [-1, -1,  0, 1, 1, 1,  0, -1]  # 상, 우상, 우, 우하, 하, 좌하, 좌, 좌상
dc = [ 0,  1,  1, 1, 0, -1, -1, -1]

while True: # 0,0이 나오면 끝내기 위해 while
    R, C = map(int, input().split())
    if R == 0 and C == 0:
        break

    field = [list(input()) for _ in range(R)]   # 지뢰 밭
    for r in range(R):
        for c in range(C):
            if field[r][c] != '*':  # 지뢰 아니면 0으로 바꿔주기
                field[r][c] = 0

    for r in range(R):
        for c in range(C):
            if field[r][c] == '*':  # 지뢰가 있다면
                for d in range(8):  # 8방향으로 지뢰 갯수 늘려줘야함
                    nr, nc = r +dr[d], c + dc[d]
                    if 0 <= nr < R and 0 <= nc < C and field[nr][nc] != '*':    # 지뢰가 아닌 곳에만 늘려주기 + 범위 체크
                        field[nr][nc] += 1

    # 출력 형식 맞춰주기
    for row in field:   # 지뢰밭 돌면서
        result = ''     # 빈 문자열 result에 담기위해
        for s in row:   # row에 있는 요소들을 s가 result에 담기, 문자열은 + 연산 가능
            result += str(s)

        print(result)
