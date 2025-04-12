'''
너무 어지러워서 지피티 써서 풀었는데 4/13 낮 중으로 다시 풀어볼 예정
'''



from collections import deque

# 상, 하, 좌, 우
# 상 = 0, 하 = 1, 좌 = 2, 우 = 3
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N = int(input())  # 보드 크기
K = int(input())  # 사과 개수

board = [[0] * N for _ in range(N)]  # 0: 빈칸, 1: 사과, 2: 뱀

for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1  # 사과 위치 (1-based -> 0-based)

L = int(input())
direction_info = dict()
for _ in range(L):
    t, d = input().split()
    direction_info[int(t)] = d

snake = deque()
snake.append((0, 0))
board[0][0] = 2  # 뱀이 처음 있는 위치

direction = 3  # 처음 방향은 오른쪽 (우 = 3)
time = 0

while True:
    time += 1
    head_r, head_c = snake[-1]
    nr = head_r + dr[direction]
    nc = head_c + dc[direction]

    # 벽 또는 자기 몸과 충돌 체크
    if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] == 2:
        break

    # 사과가 있으면 머리만 추가
    if board[nr][nc] == 1:
        board[nr][nc] = 2
        snake.append((nr, nc))
    else:
        # 사과 없으면 꼬리 제거 + 머리 추가
        tail_r, tail_c = snake.popleft()
        board[tail_r][tail_c] = 0
        board[nr][nc] = 2
        snake.append((nr, nc))

    # 방향 전환
    if time in direction_info:
        if direction_info[time] == 'L':
            if direction == 0: direction = 2
            elif direction == 1: direction = 3
            elif direction == 2: direction = 1
            elif direction == 3: direction = 0
        elif direction_info[time] == 'D':
            if direction == 0: direction = 3
            elif direction == 1: direction = 2
            elif direction == 2: direction = 0
            elif direction == 3: direction = 1

print(time)
