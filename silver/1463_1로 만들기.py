N = int(input())
dp = [0] * (N+1)
dp[1] = 0   # 1은 연산 필요 없음, dp 리스트 자체가 그 인덱스 숫자 일 때 최소 몇 번의 연산인지 저장하는 리스트

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1 # 1을 뺀 경우, 횟수 + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)  # 2로 나누어 떨어지는 경우 2로 나눈 값에서 + 1 한 값과 비교

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[N])