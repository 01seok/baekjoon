import heapq
import sys
input = sys.stdin.readline
INF = float('inf')
N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]

dist = [[INF] * N for _ in range(N)]
dist[0][0] = 0

q = [(0, 0, 0)] # cost, r, c
direct = [(0,1), (1,0)] # 오른쪽, 아래만 이동 가능

while q:
    cost, r, c = heapq.heappop(q)

    if cost > dist[r][c]:
        continue

    for dr, dc in direct:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N:
            move_cost = 0
            if field[nr][nc] >= field[r][c]:
                move_cost = field[nr][nc] - field[r][c] + 1

            new_cost = cost + move_cost

            if new_cost < dist[nr][nc]:
                dist[nr][nc] = new_cost
                heapq.heappush(q, (new_cost, nr, nc))
print(dist[N-1][N-1])