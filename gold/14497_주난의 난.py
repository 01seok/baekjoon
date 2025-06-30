from collections import deque

INF = float('inf')
N, M = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
start_r, start_c = x1 - 1, y1 - 1
goal_r, goal_c = x2 - 1, y2 - 1
class_room = [list(input()) for _ in range(N)]

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

dist = [[INF] * M for _ in range(N)]
dist[start_r][start_c] = 0
q = deque([(start_r, start_c)])

while q:
    r, c = q.popleft()

    if (r, c) == (goal_r, goal_c):
        break

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < M:
            next_pos = class_room[nr][nc]
            if next_pos == '0':
                cost = 0
            else:
                cost = 1
            next_cost = dist[r][c] + cost
            if next_cost < dist[nr][nc]:
                dist[nr][nc] = next_cost

                if cost == 0:   # 비용이 0인 경우부터 탐색하기 위해서 큐 왼쪽에 넣기
                    q.appendleft((nr, nc))
                else:           # 비용이 1인 경우, 후순위
                    q.append((nr, nc))

print(dist[goal_r][goal_c])