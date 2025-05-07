N = int(input())
result = []

def dfs(num, last_num):
    result.append(num)
    for next in range(0, last_num):
        dfs(num * 10 + next, next)

for i in range(10):
    dfs(i, i)

result.sort()

if N >= len(result):
    print(-1)
else:
    print(result[N])