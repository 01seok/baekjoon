from itertools import combinations
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

homes = []
chickens = []

for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            homes.append((r, c))
        elif city[r][c] == 2:
            chickens.append((r, c))

def 맨허튼거리(M개의치킨집):
    chicken_dist = 0
    for hr, hc in homes:
        min_dist = float('inf')
        for cr, cc in M개의치킨집:
            dist = abs(hr-cr) + abs(hc-cc)
            min_dist = min(min_dist, dist)
        chicken_dist += min_dist
    return chicken_dist

min_result = float('inf')
for 치킨집조합 in combinations(chickens, M):
    dist = 맨허튼거리(치킨집조합)
    min_result = min(min_result, dist)

print(min_result)