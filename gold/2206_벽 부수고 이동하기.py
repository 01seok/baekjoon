from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

visited = [[[0]*2 for _ in range(M)] for _ in range(N)]   # 방문 표시, 벽 부순 횟수 체크 할 visited 배열, 그래프 크기와 같게 만들기
queue = deque()
queue.append((0, 0, 0)) # r,c, 벽 부순 횟수
visited[0][0][0] = 1 # 시작점 체크

while queue:
    r, c, wall_broken = queue.popleft()

    if r == N-1 and c == M-1:   # 종료조건 : N,M 도착했을 때
        print(visited[r][c][wall_broken])   # 갈 때 마다 visited에 1씩 더 해줄거니 종료 지점의 숫자 출력하면 정답
        break

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < M:
            # 벽을 부수지 않아도 되고, 가본적이 없는 곳이라면
            if graph[nr][nc] == 0 and not visited[nr][nc][wall_broken]:
                visited[nr][nc][wall_broken] = visited[r][c][wall_broken] + 1   # 방문 체크
                queue.append((nr, nc, wall_broken))

            # 벽이 있는데 벽을 부술 수 있을 때
            elif graph[nr][nc] == 1 and wall_broken == 0 and visited[nr][nc][1] == 0:
                visited[nr][nc][1] = visited[r][c][0] + 1
                queue.append((nr, nc, 1))

else:
    print(-1)













