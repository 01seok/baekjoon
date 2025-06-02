import sys
import heapq
input = sys.stdin.readline

INF = int(21e8)

N = int(input())    # 도시 수
M = int(input())    # 버스 수
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w)) # 출발지 u에 도착지 v와 가중치 w 넣어주기

start, end = map(int, input().split())

# 다익스트라
distance = [INF] * (N+1)    # 1번부터 사용해야하니 0번 버리기 위해 N+1개
distance[start] = 0 # 출발지는 가중치 0
heap = [(0, start)] # 가중치, 출발 도시

while heap:
    cost, now = heapq.heappop(heap) # 현재 가중치와 현재 위치

    if cost > distance[now]:    # 현재 구해져있는 가중치보다 높으면 볼 필요 없음
        continue

    for next_city, weight in graph[now]:
        new_cost = cost + weight
        if new_cost < distance[next_city]:
            distance[next_city] = new_cost
            heapq.heappush(heap, (new_cost, next_city))
print(distance[end])