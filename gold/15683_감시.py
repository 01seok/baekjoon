
'''
0 : 빈칸
1 ~ 5 : cctv
6 : 벽
cctv 타입별로 회전 고려한 범위 함수 만들어서 dfs 풀기

'''

dr = [-1, 1, 0, 0]  # 0 : 상, 1 : 하, 2: 좌, 3: 우
dc = [0, 0, -1, 1]

cctv_dir = {
    1: [[0], [1], [2], [3]],    # 1번 cctv
    2: [[0, 1], [2, 3]],        # 상하, 좌우
    3: [[0, 3], [1, 3], [1, 2], [0, 2]],    # ㄴ방향
    4: [[0, 2, 3], [0, 1, 3], [1, 2, 3], [0, 1, 2]], # 3방향
    5: [[0, 1, 2, 3]]   # 4방향
}

def cctv(office, r, c, dir):
    for d in dir:
        nr, nc = r, c
        while True:
            nr += dr[d]
            nc += dc[d]
            if 0 <= nr < N and 0 <= nc < M and office[nr][nc] != 6:
                if office[nr][nc] == 0:
                    office[nr][nc] = '#'
            else:
                break

def dfs(level, office):
    global min_area

    if level == len(cctvs): # 모든 cctv 다 봤으면 최솟값 갱신 후 종료
        area = sum(row.count(0) for row in office)
        min_area = min(min_area, area)
        return

    r, c, cctv_type = cctvs[level]

    for dir in cctv_dir[cctv_type]:
        temp_office = [row[:] for row in office]    # 이번 재귀에서 사용할 맵 복사해서 사용
        cctv(temp_office, r, c, dir)    # cctv 함수 사용해서 체크하고
        dfs(level + 1, temp_office)     # 재귀 호출

N, M = map(int, input().split())    # 세로, 가로
office = [list(map(int, input().split())) for _ in range(N)]
min_area = float('inf')
cctvs = []  # cctv 있는 곳들 저장할 리스트(위치와 cctv타입)
for r in range(N):
    for c in range(M):
        if 1<= office[r][c] <= 5:
            cctvs.append((r, c, office[r][c]))

dfs(0, office)
print(min_area)