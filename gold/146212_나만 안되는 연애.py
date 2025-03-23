def find_set(x):    # union find
    if x == parent[x]:
        return x

    parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:

        return False

    if ref_x < ref_y:
        parent[ref_y] = ref_x

    else:
        parent[ref_x] = ref_y

    return True


n, m = map(int, input().split())    # 노드의 수, 간선의 수
gender = [''] + input().split()     # 성별 정보, 1번부터 사용하기 위해서 제일 앞에 빈칸 하나 추가
edges = []
for _ in range(m):
    u, v, d = map(int, input().split())
    if gender[u] != gender[v]:  # 다른 성별끼리만 간선 존재해야하니까
        edges.append((d, u, v))

parent = [i for i in range(n + 1)]

edges.sort()    # 가중치가 작은 간선부터 선택해야하므로


total_cost = 0  # 누적 가중치 저장 할 변수
edge_count = 0  # 현재까지 선택한 간선 개수 저장 할 변수 (n-1개 되면 종료)

for d, u, v in edges:
    if union(u, v):
        total_cost += d # 연결된 곳의 가중치 더해주고
        edge_count += 1 # 연결된 간선 개수 1 추가
        if edge_count == n - 1: # 모든 정점 연결 되었으면 (노드 수 - 1)
            break

if edge_count == n - 1: # 반복문 종료 후 간선 모두 연결 되었으면
    print(total_cost)   # 누적 가중치 출력

else:                   # 실패했으면 -1 출력
    print(-1)