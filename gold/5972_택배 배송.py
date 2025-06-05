import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

N, M = map(int, input().split())
adj_lst = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    adj_lst[u].append((v, w))
    adj_lst[v].append((u,w))

dist = [INF] * (N+1)
dist[1] = 0

q = [(0, 1)]

while q:
    cost, now = heapq.heappop(q)

    if dist[now] < cost:
        continue

    for next, next_cost in adj_lst[now]:
        new_cost = cost + next_cost
        if new_cost < dist[next]:
            dist[next] = new_cost
            heapq.heappush(q, (new_cost, next))

print(dist[N])