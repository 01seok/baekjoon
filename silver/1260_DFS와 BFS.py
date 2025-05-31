from collections import deque

N, M, V = map(int, input().split())
dfs_visited = [False] * (N + 1)
adj_lst = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)
for next in adj_lst:
    next.sort()

def dfs(v, dfs_visited):
    dfs_visited[v] = True
    print(v, end=' ')
    for next_v in adj_lst[v]:
        if not dfs_visited[next_v]:
            dfs(next_v, dfs_visited)

def bfs(start):
    visited = [False] * (N+1)
    q = deque([start])
    visited[start]=True
    while q:
        now_v = q.popleft()
        print(now_v, end=' ')
        for next_v in adj_lst[now_v]:
            if not visited[next_v]:
                visited[next_v]=True
                q.append(next_v)

dfs(V, dfs_visited)
print()
bfs(V)

