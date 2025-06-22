from collections import deque
N, M, K, X = map(int, input().split())

adj_lst = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    adj_lst[a].append(b)

dist = [-1] * (N+1)

q = deque([X])
dist[X] = 0

while q:
    now = q.popleft()

    for next_node in adj_lst[now]:
        if dist[next_node] == -1:
            dist[next_node] = dist[now] + 1
            q.append(next_node)

results = []
for i in range(1, N+1):
    if dist[i] == K:
        results.append(i)

if results:
    for result in results:
        print(result)
else:
    print(-1)