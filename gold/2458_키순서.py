N, M = map(int, input().split())

tall_graph = [[] for _ in range(N+1)]   # 자기보다 키 큰 사람 적을 리스트
small_graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    tall_graph[a].append(b)
    small_graph[b].append(a)

def dfs(node, visited, graph):
    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = 1
            dfs(next_node, visited, graph)

result=0
for student in range(1, N+1):   # 1번 학생부터 N번 학생까지
    bigger_visited = [0] * (N+1)
    smaller_visited = [0] * (N+1)

    bigger_visited[student] = 1
    dfs(student, bigger_visited, tall_graph)

    smaller_visited[student] = 1
    dfs(student, smaller_visited, small_graph)

    taller = sum(bigger_visited) -1 # 자기 자신 빼주기
    smaller = sum(smaller_visited) -1

    if taller + smaller == N-1: # 자기보다 큰 사람과 작은 사람을 다 안다면
        result += 1
print(result)