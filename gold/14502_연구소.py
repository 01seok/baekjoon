from collections import deque
from itertools import combinations
import copy

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

empty = []  # 빈 칸 좌표들 저장해둘 리스트
virus = []  # 바이러스 좌표 저장 리스트

for r in range(N):
    for c in range(M):
        if lab[r][c] == 0:
            empty.append((r, c))
        elif lab[r][c] == 2:
            virus.append((r, c))
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(lab_map):   # 바이러스 확산 시키고 안전지대 계산해주는 bfs 함수
    q = deque(virus)

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and lab_map[nr][nc] == 0:
                lab_map[nr][nc] = 2
                q.append((nr, nc))

    safe_area = sum(row.count(0) for row in lab_map)    # 바이러스 확산 큐 끝나면 안전지대 계산
    return safe_area

max_area = 0
for walls in combinations(empty, 3):    # 빈 칸 중 벽 3개 세우는 경우의 수
    temp_map = copy.deepcopy(lab)   # 경우의 수 마다 맵 복사해서 쓰기(원본유지)

    for r, c in walls:
        temp_map[r][c] = 1  # 3가지 경우의 수들에 벽 세우기

    area = bfs(temp_map)    # 벽 세운 맵으로 확산 시뮬레이션 진행 후 안전지대 계산
    max_area = max(max_area, area)

print(max_area)

