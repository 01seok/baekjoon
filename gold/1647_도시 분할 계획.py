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

N, M = map(int, input().split())
parents = [i for i in range(N+1)]

edges = []
for _ in range(M):
    a,b,c = map(int, input().split())
    edges.append((c, a, b)) # cost, home1, home2
edges.sort()

cnt = 0
max_cost = 0    # 가장 비싼 비용의 길을 기준으로 두 마을을 나누면 가장 적은 비용으로 가능
total_cost = 0

for cost, home1, home2 in edges:
    if find_set(home1) != find_set(home2):
        union(home1, home2)
        total_cost += cost
        max_cost = max(max_cost, cost)
        cnt += 1

    if cnt == N-1:
        break

print(total_cost-max_cost)  # 총 비용에서 제일 비싼 비용의 길 없애면 정답