N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cnt = 0 # 청소 횟수

def clean(r, c, d):
    global cnt

    if room[r][c] == 0:
        room[r][c] = 2
        cnt += 1

    for _ in range(4):
        d = (d+3) % 4   # 현재 방향에서 반시계 90도 회전
        nr,nc = r + dr[d], c+ dc[d]
        if 0<= nr < N and 0<= nc < M and room[nr][nc] == 0:
            clean(nr, nc, d)
            return

    back_d = (d+2) % 4  # 후진 방향
    br, bc = r + dr[back_d], c + dc[back_d]
    if 0<= br < N and 0<= nc < M and room[br][bc] != 1:
        clean(br, bc, d)    # 후진 할 때는 방향 유지
    else:
        return  # 후진해도 벽이면 종료

clean(r, c, d)
print(cnt)