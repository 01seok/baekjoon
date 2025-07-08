T = int(input())
for tc in range(T):
    N = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]

    if N == 1:
        print(max(stickers[0][0],stickers[1][0]))
        continue

    dp = [[0] * N for _ in range(2)]
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]

    dp[1][1] = stickers[1][1] + stickers[0][0]
    dp[0][1] = stickers[0][1] + stickers[1][0]

    for i in range(2, N):
        dp[0][i] = stickers[0][i] + max(dp[1][i-1], dp[1][i-2])
        dp[1][i] = stickers[1][i] + max(dp[0][i-1], dp[0][i-2])

    print(max(dp[0][N-1], dp[1][N-1]))