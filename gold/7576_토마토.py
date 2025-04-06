from collections import deque

M, N = map(int, input().split())
tomato_box = [list(map(int, input().split())) for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

queue = deque()

for r in range(N):
    for c in range(M):
        if tomato_box[r][c] == 1:
            queue.append((r, c))    # 익은 토마토들을 큐에 넣고

while queue:    #  큐가 빌 때 까지 bfs
    r, c = queue.popleft()

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < M:
            if tomato_box[nr][nc] == 0:
                tomato_box[nr][nc] = tomato_box[r][c] + 1
                queue.append((nr, nc))

cnt = 0 # 토마토가 전부 다 익는데 걸린 시간 더하면서 갱신해줄 변수

for r in range(N):
    for c in range(M):
        if tomato_box[r][c] == 0:   # bfs 돌았는데도 익지 않은 토마토가 있다면
            print(-1)   # 불가능한 상황
            exit()      # 코드 종료
        cnt = max(tomato_box[r][c], cnt)    # 반복문 다 돌고나면 지금까지 1씩 더 해왔으므로 며칠이 걸렸는지 갱신 돼 있음
print(cnt-1)    # 처음 시작이 1이었으므로 소요된 날짜는 -1일 해주기