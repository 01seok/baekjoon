N = int(input())
dp = [0] * (N+1)
dp[1] = 1

if N>= 2:   # N = 1인 경우, 에러 방지
    dp[2] = 2

for i in range(3, N+1):
    # dp[3]의 경우 dp[2]만큼 채우고나면 dp[1]만큼의 공간만 남기 때문에
    dp[i] = dp[i-1] + dp[i-2]   # dp[i]는 dp[i-1]의 경우의 수 + dp[i-2]의 경우의 수

print(dp[N] % 10007)