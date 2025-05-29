standard = [1, 1, 2, 2, 2, 8]
found = list(map(int, input().split()))
result = [s - f for s, f in zip(standard, found)]
print(*result)