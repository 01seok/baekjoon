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

while True:
    M, N = map(int, input().split())
    if (M, N) == (0, 0):
        break

    parents = list(range(M))    # 0번부터 M-1번 집
    edges = []
    total_cost = 0

    for _ in range(N):
        x,y,z = map(int, input().split())
        edges.append((z, x, y))
        total_cost += z # 모든 도로를 그대로 썼을 때의 비용을 구하기 위해 더하기

    edges.sort()
    min_cost = 0
    for cost, home1, home2 in edges:
        if find_set(home1) != find_set(home2):
            union(home1, home2)
            min_cost += cost

    print(total_cost - min_cost)