from collections import deque

N, M = map(int, input().split())    # 가로 세로
treasure_map = [list(input()) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(start_row, start_col):
    visited = [[0] * M for _ in range(N)]   # 방문 체크 할 2차원 배열
    queue = deque() # bfs를 위한 큐 초기화 (행, 열, 이동거리)
    queue.append((start_row, start_col, 0))
    visited[start_row][start_col] = 1   # 시작지점 방문 체크
    max_distance = 0    # 시작지점부터 이동거리 갱신 할 변수

    while queue:
        r, c, dist = queue.popleft()
        max_distance = max(max_distance, dist)

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < M:
                if visited[nr][nc] == 0 and treasure_map[nr][nc] == 'L':    # 방문하지 않았고 육지라면
                    visited[nr][nc] = 1 # 방문 체크하고
                    queue.append((nr, nc, dist + 1))    # 다음 좌표와 이동거리 +1해서 큐에 추가
    return max_distance

result = 0

for r in range(N):
    for c in range(M):
        if treasure_map[r][c] == 'L':
            result = max(result, bfs(r, c))

print(result)

