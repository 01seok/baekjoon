T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T + 1):
    M, N, K = map(int, input().split())

    adj = []
    for _ in range(K):
        c, r = map(int, input().split())    # x, y 좌표
        adj.append((r, c))  # r,c 기준으로 adj 리스트에 넣어주기

    field = [[0] * M for _ in range(N)] # 배추 밭 2차원 배열 입력
    for i in range(K):  # adj 리스트 = 배추가 있는 곳, 1로 체크 해주기
        r, c = adj[i]
        field[r][c] = 1

    cnt = 0 # 정답, 배추 무리 체크할 변수
    for r in range(N):
        for c in range(M):
            if field[r][c] == 1:    # 배추가 있으면
                stack = [(r, c)]    # 스택에 넣고
                field[r][c] = 0     # 방문한 배추 0으로 변경

                while stack:        # 스택 빌 때 까지(이 문제에선 이번 배추 주변 다 체크할 때 까지)
                    real_r, real_c = stack.pop()    # 델타 배열에서 사용할 지금 배추 위치 변수
                    for d in range(4):              # 상하좌우 탐색
                        nr, nc = real_r + dr[d], real_c + dc[d]
                        if 0<= nr < N and 0 <= nc < M and field[nr][nc] == 1:   # 1 = 주변 4방향 중 배추가 있을 때
                            field[nr][nc] = 0   # 방문 배추 체크하고
                            stack.append((nr, nc))  # 다음 칸에도 배추 있는지 다시 while문 출발
                cnt += 1    # while문 한번 끝날때마다 배추 무리 1 증가
    print(cnt)