import heapq
import sys
input = sys.stdin.readline
INF = float('inf')

N, M = map(int, input().split())
sight = list(map(int, input().split())) # 각 노드 별 시야 정보

sight[-1] = 0   # 넥서스는 시야 보여도 상관 없음

adj_lst = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    adj_lst[a].append((b, t))
    adj_lst[b].append((a, t))    # 양방향 그래프

dist = [INF] * N
dist[0] = 0 # 출발지는 시간 0초
q = [(0, 0)]    # 시간, 현재 위치

while q:
    time, now = heapq.heappop(q)

    if dist[now] < time:
        continue

    for next, t in adj_lst[now]:

        if sight[next]: # 시야 있는 곳이면 pass
            continue

        if dist[next] > dist[now] + t:
            dist[next] = dist[now] + t
            heapq.heappush(q, (dist[next], next))

if dist[N-1] != INF:
    print(dist[N-1])
else:
    print(-1)