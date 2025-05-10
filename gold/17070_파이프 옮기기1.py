N = int(input())    # 집의 크기
house = [list(map(int, input().split())) for _ in range(N)]

# 처음 출발지는 (1,1), (1,2)
# 빈칸 0, 벽 1
# 방향 3개 가로 세로 대각선
# 방향 번호 부여 가로 : 0, 세로 : 1, 대각선 : 2
# 출력 : 방법의 수, 없으면 0

cnt = 0

def dfs(r, c, dir):
    global cnt

    if r == N-1 and c == N-1:
        cnt += 1
        return

    # 가로 방향
    if dir == 0 or dir == 2:
        nr, nc = r, c+1
        if nc < N and house[nr][nc] == 0:
            dfs(nr, nc, 0)

    # 세로 방향
    if dir == 1 or dir == 2:
        nr, nc = r+1, c
        if nr < N and house[nr][nc] == 0:
            dfs(nr, nc, 1)


    # 둘 다 가능한 대각선
    nr, nc = r+1, c+1
    if nr < N and nc < N:
        if house[r+1][c] == 0 and house[r][c+1] == 0 and house[nr][nc] == 0:
         dfs(nr, nc, 2)

dfs(0,1,0)
print(cnt)