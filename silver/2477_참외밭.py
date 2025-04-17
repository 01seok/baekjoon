K = int(input())
chamoe = [list(map(int, input().split())) for _ in range(6)]
max_w = 0
max_h = 0
max_w_idx = -1
max_h_idx = -1

# 제일 큰 가로 세로 길이
for r in range(6):
    d, length = chamoe[r]
    if d in (1, 2): # 가로
        if length > max_w:
            max_w = length
            max_w_idx = r
    elif d in (3, 4): # 세로
        if length > max_h:
            max_h = length
            max_h_idx = r

# 비어있는 면적 가로 세로 길이 구하기
# 큰 세로 양 옆은 작은 가로 2개, 큰 가로 양 옆은 작은 세로 2개, 인덱스 순환을 위해 % 6
min_w = abs(chamoe[(max_h_idx-1) % 6][1] - chamoe[(max_h_idx+1) % 6][1])
min_h = abs(chamoe[(max_w_idx-1) % 6][1] - chamoe[(max_w_idx +1) %6][1])

result = (max_w * max_h) - (min_h * min_w)
print(result*K)