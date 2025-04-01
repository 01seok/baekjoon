w, h = map(int, input().split())    # 가로 세로
N = int(input())
rows = [0, h]   # 세로 자를 포인트 저장할 리스트
cols = [0, w]   # 가로 자를 포인트 저장할 리스트

for _ in range(N):
    d, pos = map(int, input().split())
    if d == 0:
        rows.append(pos)
    else:
        cols.append(pos)

rows.sort() # 순서대로 정렬해서
cols.sort()

# 앞뒤로 빼면 높이, 너비 나옴
max_height = max(rows[i+1] - rows[i] for i in range(len(rows)-1))
max_width = max(cols[i+1] - cols[i] for i in range(len(cols)-1))

print(max_height * max_width)