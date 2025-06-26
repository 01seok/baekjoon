def find_set(x):
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):

    root_x = find_set(x)
    root_y = find_set(y)

    if root_x == root_y:
        return

    if root_x < root_y:
        parents[root_y] = root_x

    else:
        parents[root_x] = root_y

N = int(input())
cost_map = [list(map(int, input().split())) for _ in range(N)]

edges = []
for i in range(N):
    for j in range(i+1, N): # cost_map은 대칭인데 최소 관리 비용이니 중복되는 비용은 담지 않고, 자기자신 연결은 필요 없으니 제거
        edges.append((cost_map[i][j], i, j))

edges.sort()
parents = list(range(N))
min_cost = 0
cnt = 0

for w, u, v in edges:
    if find_set(u) != find_set(v):
        union(u, v)
        min_cost += w
        cnt += 1
        if cnt == N-1:
            break

print(min_cost)