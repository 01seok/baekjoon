import math

room_number = input()
counts = [0] * 10   # 카운팅 배열

for i in room_number:
    counts[int(i)] += 1

# 6과 9는 서로 대체 가능하므로 합산 후 2로 나눈 후 올림.
counts[6] = math.ceil((counts[6] + counts[9]) / 2)

# 최댓값 구하기 (9는 이미 6이랑 합산되어있음)
print(max(counts[:9]))