from collections import deque

N = int(input())    # 총 인원
M = int(input())

adj_lst = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)    # 친구 관계, 양 방향 그래프

visited = [False] * (N+1)   # 0번부터 시작, 0번 버리기
visited[1] = True   # 본인 방문 체크

q = deque()
q.append((1, 0))    # 본인부터 시작(현재 위치, 친구 깊이, 1 넘으면 초대x)
cnt = 0 # 결혼식 초대 인원
while q:
    now, friendship = q.popleft()
    if friendship >= 2:
        continue

    for next_friend in adj_lst[now]:   # 현재 친구의 관계 체크
        if not visited[next_friend]:    # 확인 안한 사람
            visited[next_friend] = True
            cnt += 1
            q.append((next_friend,friendship+1))    # 친구의 친구니까 관계 +1해서 얘로 인해서 아는 친구 초대 하면 안됨
print(cnt)