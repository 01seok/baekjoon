import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

V, E = map(int, input().split())
K = int(input())
adj_lst = [[] for _ in range(V+1)]
dist = [INF] * (V+1)

for _ in range(E):
    u,v,w = map(int, input().split())
    adj_lst[u].append((v,w))    # 양방향 그래프라는 말 없음

q = []
heapq.heappush(q, (0, K))   # 현재 가중치, 현재 노드
dist[K] = 0 # 자기 자신은 가중치 0

while q:
    cost, now = heapq.heappop(q)

    if dist[now] < cost:    # 이미 더 최소 값으로 가는 경로가 있었다면 볼 필요 없음
        continue

    for next, weight in adj_lst[now]:   # 다음 노드, 가중치를 현재 노드 기준 리스트에서 확인
        new_cost = dist[now] + weight

        # 더 짧은 경로 있다면 갱신해서 최소힙에 넣어주기
        if dist[next] > new_cost:
            dist[next] = new_cost
            heapq.heappush(q,(new_cost, next))

for i in range(1, V+1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])