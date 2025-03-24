import sys
sys.setrecursionlimit(10**5)    # 문제 조건 10만까지

def dfs(num):
    global cnt

    if cnt == N:    # 모든 정점에 번호가 있으면 return
        return

    for next_num in graph[num]:
        if visited[next_num] == 0:  # 방문한 적 없다면
            cnt += 1
            visited[next_num] = cnt # 다음 번호를 visited 배열에 적어주기
            dfs(next_num)   # 재귀

N, M, R = map(int, input().split()) # 정점의 수, 간선의 수, 시작 정점
graph = [[] for _ in range(N + 1)]  # 1 ~  N번 그래프
for _ in range(M):
    u, v = map(int, input().split())    # 간선 정보
    graph[u].append(v)  # 양방향 간선이니 서로 더해주기
    graph[v].append(u)

for i in range(1, N + 1):   # 1번부터 N번까지 내림차순으로 방문하기 위해 내림차순 정렬
    graph[i].sort(reverse=True)

visited = [0] * (N + 1)     # 방문 번호를 남길 visited 배열
cnt = 1 # 방문 번호, 1번부터 시작
visited[R] = cnt    # 시작 정점은 1번
dfs(R)  # 재귀호출

for i in range(1, N + 1):
    print(visited[i])