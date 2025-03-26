def dfs(node):
    visited[node] = 1
    for next_node in graph[node]:
        if visited[next_node] == 0:
            dfs(next_node)

N = int(input())    # 컴퓨터의 수
M = int(input())    # 간선 수, 1번부터 시작

graph = [[] for _ in range(N + 1)]  # 그래프 수
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향 그래프이므로 서로 넣어주기

visited = [0] * (N+1)   # 방문한 배열은 1이 될거고 1의 개수를 구하면 정답

dfs(1)
for i in visited:
    result = visited.count(1)
print(result - 1)