import sys
sys.setrecursionlimit(10**5)  # 재귀 제한 증가
input = sys.stdin.readline

dr = [-1, 1, 0, 0, -1, -1, 1, 1]    # 상 하 좌 우 좌상 우상 좌하 우하
dc = [0, 0, -1, 1, -1, 1, -1, 1]

def dfs(r, c):
    visited[r][c] = True
    for d in range(8):
        nr, nc = r +dr[d], c +dc[d]
        if 0<=nr <h and 0<= nc < w:
            if not visited[nr][nc] and world[nr][nc] == 1:
                dfs(nr, nc)

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    world = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    cnt = 0
    for r in range(h):
        for c in range(w):
            if world[r][c] == 1 and not visited[r][c]:
                dfs(r,c)
                cnt += 1
    print(cnt)