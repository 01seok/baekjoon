from collections import deque

N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

max_h = max(map(max, area)) # 최고 높이, 이 높이까지 잠기는 시뮬레이션 실행 예정
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c, h, visited):
    q= deque()
    q.append((r, c))
    visited[r][c] = True

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r +dr[d], c +dc[d]
            if 0<= nr < N and 0<= nc < N:
                if not visited[nr][nc] and h < area[nr][nc]:    # 현재 잠기는 위치보다 높으면 안전지대
                    visited[nr][nc] = True
                    q.append((nr, nc))
max_safe_zone = 0

for h in range(max_h +1):   # 잠기는 높이 별 안전 지대 구하기
    visited = [[False] * N for _ in range(N)]
    safe_zone = 0
    for r in range(N):
        for c in range(N):
            if not visited[r][c] and area[r][c] > h:
                bfs(r,c,h, visited) # 방문하지 않은 안전지대라면 인접한 안전지대 묶어주기
                safe_zone += 1
    max_safe_zone = max(max_safe_zone, safe_zone)
print(max_safe_zone)