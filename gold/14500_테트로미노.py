N, M = map(int,input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
max_sum = 0
tetromino = [
    # ㅡ, ㅣ
    [(0,0), (0,1), (0,2), (0,3)],
    [(0,0), (1,0), (2,0), (3,0)],
    # ㅁ
    [(0,0), (0,1), (1,0), (1,1)],
    # L
    [(0,0), (1,0), (2,0), (2,1)],
    [(0,0), (1,0), (2,0), (2,-1)],
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (1,0), (2,0)],
    [(0,0), (0,1), (0,2), (1,0)],
    [(0,0), (0,1), (0,2), (1,2)],
    [(0,0), (1,0), (1,1), (1,2)],
    [(0,2), (1,0), (1,1), (1,2)],
    # 번개
    [(0,0), (0,1), (1,1), (1,2)],
    [(0,1), (0,2), (1,0), (1,1)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(0,1), (1,1), (1,0), (2,0)],
    # ㅜ
    [(0,0), (0,1), (0,2), (1,1)],
    [(1,0), (1,1), (1,2), (0,1)],
    [(0,0), (1,0), (2,0), (1,1)],
    [(0,1), (1,1), (2,1), (1,0)],
]

for r in range(N):
    for c in range(M):
        for shape in tetromino:
            total = 0
            for dr, dc in shape:
                nr, nc = r+ dr, c +dc
                if 0<=nr<N and 0<=nc<M:
                    total += paper[nr][nc]

            max_sum = max(max_sum, total)

print(max_sum)