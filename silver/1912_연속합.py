N = int(input())
arr = list(map(int, input().split()))

dp = [0] * N
dp[0] = arr[0]
max_sum = arr[0]

for i in range(1, N):
    dp[i] = max(arr[i], dp[i-1] + arr[i])
    max_sum = max(max_sum, dp[i])
print(max_sum)