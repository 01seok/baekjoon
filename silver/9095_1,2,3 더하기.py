T = int(input())
nums = [int(input()) for _ in range(T)]
max_n = max(nums)

dp = [0] * (max_n + 1)
dp[0] = 1   # 아무것도 선택하지 않는 경우 = 한 가지 경우

for i in range(1, max_n+1):

    if i >= 1:  # 마지막에 1을 더해서 만들 수 있는 경우의 수
        dp[i] += dp[i-1]

    if i >= 2:  # dp에 2를 더해서 만들 수 있는 경우의 수
        dp[i] += dp[i-2]

    if i >= 3:  # dp에 3을 더해서 만들 수 있는 경우의 수
        dp[i] += dp[i-3]

for n in nums:
    print(dp[n])