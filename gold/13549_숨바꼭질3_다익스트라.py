import heapq

N,K = map(int, input().split())
dist = [100001] * 100001
dist[N] = 0
q = []
heapq.heappush(q, (0, N))   # 시간, 위치

while q:
    time, now = heapq.heappop(q)

    if now == K:
        print(time)
        break

    if time > dist[now]:    # 최소 시간 아니면 pass
        continue

    next = now * 2
    if 0 <= next < 100001 and time < dist[next]:
        dist[next] = time
        heapq.heappush(q, (time, next))


    for next in (now -1, now + 1):
        if 0<= next < 100001 and time + 1 < dist[next]:
            dist[next] = time + 1
            heapq.heappush(q, (time+1, next))