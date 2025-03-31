T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T + 1):
    M, N, K = map(int, input().split())

    adj = []
    for _ in range(K):
        c, r = map(int, input().split())    # x, y 좌표
        adj.append((r, c))

    field = [[0] * M for _ in range(N)]
    for i in range(K):
        r, c = adj[i]
        field[r][c] = 1

    cnt = 0
    for r in range(N):
        for c in range(M):
            if field[r][c] == 1:
                stack = [(r, c)]
                field[r][c] = 0

                while stack:
                    real_r, real_c = stack.pop()
                    for d in range(4):
                        nr, nc = real_r + dr[d], real_c + dc[d]
                        if 0<= nr < N and 0 <= nc < M and field[nr][nc] == 1:
                            field[nr][nc] = 0
                            stack.append((nr, nc))
                cnt += 1
    print(cnt)