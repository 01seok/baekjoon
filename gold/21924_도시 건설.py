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
village = []

total_cost = 0
for _ in range(M):
    u,v,w = map(int, input().split())
    village.append((w,u,v))
    total_cost += w

village.sort()

parents = list(range(N+1))

cnt = 0
mst_cost = 0

for w, u, v in village:
    if find_set(u) != find_set(v):
        union(u, v)
        mst_cost += w
        cnt += 1

        if cnt == N-1:
            break

if cnt != N-1:
    print(-1)
else:
    print(total_cost - mst_cost)