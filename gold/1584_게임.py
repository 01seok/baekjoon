import sys
import heapq
input = sys.stdin.readline

INF = float('inf')
size = 501
board = [[0] * size for _ in range(size)]
dist = [[INF] * size for _ in range(size)]

N = int(input())
for _ in range(N):  # 위험 구역 체크
    x1, y1, x2, y2 = map(int, input().split())
    x_start, x_end = min(x1, x2), max(x1, x2)
    y_start, y_end = min(y1, y2), max(y1, y2)
    for r in range(x_start, x_end+1):
        for c in range(y_start, y_end+1):
            if board[r][c] == 0:   # 죽음 구역 아니면
                board[r][c] = 1     # 위험 구역 처리

M = int(input())
for _ in range(M):  # 죽음 구역 체크
    x1, y1, x2, y2 = map(int, input().split())
    x_start, x_end = min(x1, x2), max(x1, x2)
    y_start, y_end = min(y1, y2), max(y1, y2)
    for r in range(x_start, x_end+1):
        for c in range(y_start, y_end+1):
            board[r][c] = -1     # 죽음 구역 처리

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
q = [(0, 0, 0)]   # cost, r, c
dist[0][0] = 0

while q:
    cost, r, c = heapq.heappop(q)

    if (r, c) == (500, 500):
        print(cost)
        exit()

    if cost > dist[r][c]:
        continue

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]

        if 0 <= nr < size and 0 <= nc < size:
            if board[nr][nc] == -1:
                continue

            new_cost = cost + board[nr][nc]
            if new_cost < dist[nr][nc]:
                dist[nr][nc] = new_cost
                heapq.heappush(q, (new_cost, nr, nc))

print(-1)   # 갈 수 없다면 -1 출력