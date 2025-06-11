N = int(input())

result = 0  # 생성자가 없으면 0

for M in range(1, N):
    total = M + sum(map(int, str(M)))  # 분해합 = M + M의 각 자리수 합
    if total == N:
        result = M
        break  # 가장 작은 생성자를 찾으면 종료

print(result)