from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

q = deque()
q.append((0, 0))

while q:
    r, c = q.popleft()

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]

        if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] == 1:
            maze[nr][nc] = maze[r][c] + 1
            q.append((nr, nc))

print(maze[N-1][M-1])