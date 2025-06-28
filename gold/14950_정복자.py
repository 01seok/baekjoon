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

N, M, t = map(int, input().split())
edges = []
for _ in range(M):
    a,b,c = map(int, input().split())
    edges.append((c,a,b))

edges.sort()
parents = list(range(N+1))  # 1번 부터

cnt = 0
mst_sum = 0

for w,u,v in edges:
    if find_set(u) != find_set(v):
        union(u, v)
        mst_sum += w + (cnt * t)
        cnt += 1
        if cnt == N-1:
            break
print(mst_sum)