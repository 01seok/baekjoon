N, M = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            total = cards[i] + cards[j] + cards[k]
            if total <= M:
                max_sum = max(max_sum, total)

print(max_sum)