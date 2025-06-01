from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N = int(input())
field = [list(input()) for _ in range(N)]

def bfs(r, c, visited, field, is_color_blindness):
    q = deque()
    q.append((r, c))
    visited[r][c] = True
    current_color = field[r][c]

    while q:
        cr, cc = q.popleft()
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0<= nr < N and 0<= nc < N and not visited[nr][nc]:
                next_color = field[nr][nc]
                if is_color_blindness:  #  색약인 경우
                    if (current_color in "RG" and next_color in "RG") or (current_color in "B" and next_color in "B"):
                        visited[nr][nc] = True
                        q.append((nr, nc))
                else:
                    if current_color == next_color:
                        visited[nr][nc] = True
                        q.append((nr, nc))
visited_normal_case = [[False] * N for _ in range(N)]
cnt_normal_case = 0
for r in range(N):
    for c in range(N):
        if not visited_normal_case[r][c]:
            bfs(r, c, visited_normal_case, field, is_color_blindness=False)
            cnt_normal_case += 1

visited_blindness_case = [[False] * N for _ in range(N)]
cnt_blindness_case = 0
for r in range(N):
    for c in range(N):
        if not visited_blindness_case[r][c]:
            bfs(r, c, visited_blindness_case, field, is_color_blindness=True)
            cnt_blindness_case += 1

print(cnt_normal_case, cnt_blindness_case)