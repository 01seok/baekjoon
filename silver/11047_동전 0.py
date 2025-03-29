N, K = map(int, input().split())    # 동전의 종류 N, 만들어야하는 숫자 K
coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)

total = 0
cnt = 0

for i in range(N):
        if total == K:
            break

        if K >= coins[i]:
            j = K // coins[i]
            total += coins[i] * j
            K -= coins[i] * j
            cnt += j


print(cnt)