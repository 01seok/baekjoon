from collections import deque

N, M = map(int, input().split())    # 노드 개수, 간선 개수
adj_lst = [[] for _ in range(N + 1)]    # 인접 리스트, 1번부터 시작이니 0번 사용 안함
for _ in range(M):
    s, e = map(int, input().split())
    adj_lst[s].append(e)
    adj_lst[e].append(s)

visited = [-1] * (N+1)  # 방문 배열이자 거리가 얼마나 되는지 체크할 배열
visited[1] = 0  # 시작 집은 1번 노드 고정이고 거리 0

queue =deque([1])   # 1번 노드부터 bfs 시작

while queue:
    current = queue.popleft()
    for next_node in adj_lst[current]:
        if visited[next_node] == -1:    # 방문하지 않은 곳이라면
            visited[next_node] = visited[current] + 1   # 현재 있는 곳 보다 한 칸 더 멀리 있는 노드
            queue.append(next_node)
max_dist = max(visited[1:]) # 1번 노드부터 끝까지 보았을 때 가장 먼 거리
house_num = visited.index(max_dist) # 가장 멀리있는 노드 번호 찾기
cnt = visited[1:].count(max_dist)   # 가장 먼 거리 몇개 있는지
print(house_num, max_dist, cnt)