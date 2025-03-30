import sys
sys.setrecursionlimit(10**5)

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

V, E = map(int, input().split())
parents = [i for i in range(V + 1)]

edges = []
for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()


cnt = 0
weight = 0
for c, a, b in edges:
    if find_set(a) != find_set(b):
        union(a, b)
        cnt += 1
        weight += c
    if cnt == V - 1:
        break
print(weight)