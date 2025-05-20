from collections import deque

N, M = map(int, input().split())
adj_lst = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    adj_lst[u].append(v)
    adj_lst[v].append(u)

visited = [False] * (N+1)

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        now = q.popleft()
        for next in adj_lst[now]:
            if not visited[next]:
                visited[next] = True
                q.append(next)

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        cnt += 1
print(cnt)