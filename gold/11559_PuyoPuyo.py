from collections import deque
row, col = 12, 6
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
field = [list(input()) for _ in range(row)]
cnt = 0

def bfs(r, c, visited):
    q = deque()
    q.append((r,c))
    visited[r][c] = 1
    color = field[r][c]
    check_lst = [(r,c)] # 색깔 겹치는게 몇개인지 확인할 리스트

    while q:
        cur_r, cur_c = q.popleft()
        for d in range(4):
            nr, nc = cur_r + dr[d], cur_c +dc[d]
            if 0 <= nr < row and 0<= nc < col:
                if visited[nr][nc] == 0 and field[nr][nc] == color:
                    visited[nr][nc] = 1
                    q.append((nr, nc))
                    check_lst.append((nr, nc))
    if len(check_lst) >= 4:
        for check_r, check_c in check_lst:
            field[check_r][check_c] = '.'
        return True

    return False    # 못 터트렸을 때

def gravity():
    for c in range(col):
        fall_lst = []   # 떨어질 블록 모아둘 리스트
        # 밑에서 위로 올라가며 떨어질 블록 모으기
        for r in range(row-1, -1, -1):
            if field[r][c] != '.':
                fall_lst.append(field[r][c])

        r = row -1  # 밑에서부터 채우기
        for block in fall_lst:
            field[r][c] = block
            r -= 1

        # 남은 위쪽 칸들은 .으로 만들어주기
        for i in range(r, -1, -1):
            field[i][c] = '.'


while True:
    visited = [[0] * col for _ in range(row)]
    flag = False # 이번 턴에 뿌요했는지 체크할 플래그

    for r in range(row):
        for c in range(col):
            if field[r][c] != '.' and visited[r][c] == 0:
                if bfs(r, c, visited):
                    flag = True
    if not flag:    # 더이상 뿌요할거 없으면 끝내기
        break

    gravity()
    cnt += 1
print(cnt)