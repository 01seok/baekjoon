N = int(input())
answer = -1
for i in range(N//5, -1, -1):
    rest = N - 5 * i
    if rest % 3 == 0:
        answer = i + (rest // 3)
        break

print(answer)