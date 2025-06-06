import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

N, E = map(int, input().split())
adj_lst = [[] for _ in range(N+1)]

for _ in range(E):
    u,v,w = map(int, input().split())
    adj_lst[u].append((v, w))
    adj_lst[v].append((u, w))

v1, v2 = map(int, input().split())  # 꼭 지나야하는 두 정점

def dijkstra(start):
    dist = [INF] * (N+1)
    dist[start] = 0 # 출발지의 가중치는 0
    heap = [(0, start)]  # 가중치, 출발 위치

    while heap:
        cost, now = heapq.heappop(heap)

        if dist[now] < cost:
            continue

        for next, weight in adj_lst[now]:
            new_cost = cost + weight
            if dist[next] > new_cost:
                dist[next] = new_cost
                heapq.heappush(heap, (new_cost, next))
    return dist

dist1 = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

ans1 = dist1[v1] + dist_v1[v2] + dist_v2[N]
ans2 = dist1[v2] + dist_v2[v1] + dist_v1[N]

ans = min(ans1, ans2)

if ans < INF:
    print(ans)
else:
    print(-1)