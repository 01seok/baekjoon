import sys
import heapq

M, N = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

INF = float('inf')
dist = [[INF] * M for _ in range(N)]
dist[0][0] = 0  # 첫 출발지는 벽 부순 횟수 0

q = []
heapq.heappush(q, (0,0,0))  # 벽 부순 횟수, r, c

while q:
    cost, r, c = heapq.heappop(q)

    if r == N-1 and c == M-1:
        print(cost)
        break

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]

        if 0 <= nr < N and 0 <= nc < M:
            new_cost = cost + maze[nr][nc]
            if new_cost < dist[nr][nc]:
                dist[nr][nc] = new_cost
                heapq.heappush(q, (new_cost,nr, nc))