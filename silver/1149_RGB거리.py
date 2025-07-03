N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]  # 각 집의 색깔 별 색칠 비용
dp = [[0] * 3 for _ in range(N)]    # 3 색, 각 집 마다 색칠 비용

# 첫 번째 집을 빨간색, 초록색, 파란색으로 칠했을 경우 dp 배열
dp[0][0] = cost[0][0]
dp[0][1] = cost[0][1]
dp[0][2] = cost[0][2]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

print(min(dp[N-1]))