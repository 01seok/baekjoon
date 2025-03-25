arr = [list(map(int, input().split())) for _ in range(9)]

max_num = -1
max_now = (0, 0)
for r in range(9):
    for c in range(9):
        if arr[r][c] > max_num:
            max_num = arr[r][c]
            max_now = (r+1, c+1)
print(max_num)
print(*max_now)