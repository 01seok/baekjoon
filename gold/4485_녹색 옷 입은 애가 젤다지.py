import sys
import heapq
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
INF = float('inf')
tc = 1

while True:
    N = int(input())
    if N == 0:
        break

    cave = [list(map(int, input().split())) for _ in range(N)]
    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = cave[0][0]

    q = []
    heapq.heappush(q, (cave[0][0], 0, 0))   # cost, r, c

    while q:
        cost, r, c = heapq.heappop(q)

        if dist[r][c] < cost:   # 이 전에 왔을 때의 가중치가 더 낮다면 pass
            continue

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                new_cost = cave[nr][nc] + cost
                if new_cost < dist[nr][nc]: # 이 전에 왔을 때의 가중치보다 낮다면 new_cost로 갱신
                    dist[nr][nc] = new_cost
                    heapq.heappush(q, (new_cost, nr, nc))

    print(f'Problem {tc}: {dist[N-1][N-1]}')
    tc += 1