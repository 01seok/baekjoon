def dfs(day, pay):
    global max_pay

    if day >= N:
        max_pay = max(max_pay, pay)
        return

    if day + T[day] <= N:   # 수락한 경우
        dfs(day + T[day], pay + P[day])

    dfs(day + 1, pay)   # 수락하지 않은 경우


N = int(input()) # N일동안 출근
T = []  # 소요 날짜 담을 리스트
P = []  # 받는 페이 담을 리스트
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

max_pay = 0
dfs(0, 0)
print(max_pay)