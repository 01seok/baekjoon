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

N = int(input())    # 컴퓨터 수
M = int(input())    # 간선 수

parents = [i for i in range(N+1)]   #  자기 자신을 부모로하는 부모 리스트

edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b)) # cost, com1, com2

edges.sort()    # 최소 비용을 위해 오름차순 정렬

cnt = 0
total_cost = 0

for cost, a, b in edges:
    if find_set(a) != find_set(b):  # 서로 연결 되지 않았다면
        union(a, b)
        total_cost += cost
        cnt += 1

        if cnt == N-1:
            break
print(total_cost)