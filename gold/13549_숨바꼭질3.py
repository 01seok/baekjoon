from collections import deque
N, K = map(int, input().split())
visited = [-1] * 100001
q = deque()
q.append(N)
visited[N] = 0

while q:
    now_N = q.popleft()

    if now_N == K:
        print(visited[now_N])
        break

    for next_N in (now_N-1, now_N+1, 2*now_N):
        if 0<= next_N < 100001 and visited[next_N] == -1:
            if next_N == 2 * now_N:
                visited[next_N] = visited[now_N]
                q.appendleft(next_N)
            else:
                visited[next_N] = visited[now_N] + 1
                q.append(next_N)