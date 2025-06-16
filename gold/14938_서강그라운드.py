import sys
import heapq

INF = float('inf')
N, M, R = map(int, input().split()) # 노드 개수, 갈 수 있는 가중치, 간선의 개수
items = list(map(int, input().split())) # 각 노드 별 아이템 개수
adj_lst = [[] for _ in range(N+1)]  # 0번 사용하지 않으므로 N+1개
for _ in range(R):
    u, v, w = map(int, input().split())
    adj_lst[u].append((v, w))
    adj_lst[v].append((u, w))

def dijkstra(start):
    dist = [INF] * (N+1)
    dist[start] = 0
    q = [(0, start)]    # 누적 가중치, 출발 노드

    while q:
        cost, now = heapq.heappop(q)
        if dist[now] < cost:
            continue

        for next_node, weight in adj_lst[now]:
            new_cost = cost + weight
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(q, (new_cost, next_node))
    return dist

max_item = 0    # 최대 아이템 개수(정답)
for i in range(1, N+1): # 어느 노드에서 시작하는지 1번 노드부터 N번 노드까지 다 체크
    dist = dijkstra(i)  # 다익스트라 해본 후
    total = 0
    for j in range(1, N+1): # 탐색 범위 내에 있는 아이템들 합치기 위한 반복문
        if dist[j] <= M:
            total += items[j-1]
    max_item = max(max_item, total)
print(max_item)