import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
adj_lst = [[] for _ in range(N+1)]
INF = float('inf')

for _ in range(M):
    a, b, c = map(int, input().split())
    adj_lst[a].append((b, c))
    adj_lst[b].append((a, c))

s, t = map(int, input().split())    # s 시작 정점, t = 종료 정점

dist = [INF] * (N+1)
dist[s] = 0
q = [(0, s)]

while q:
    cost, now = heapq.heappop(q)

    if dist[now] < cost:
        continue

    for next, weight in adj_lst[now]:
        new_cost = cost + weight
        if new_cost < dist[next]:
            dist[next] = new_cost
            heapq.heappush(q, (new_cost, next))

print(dist[t])
