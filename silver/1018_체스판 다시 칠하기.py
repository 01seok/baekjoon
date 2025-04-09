N, M = map(int, input().split())    # N,M은 8이상 50 이하, N=행, M=열
board = [list(input()) for _ in range(N)]
min_cost = 64   # 최악의 경우 8x8 다 색칠해야함
for r in range(N-7):    # 몇번 이동하면서 8칸 만들 수 있는지 봐야 하므로 (최소 8칸, 8칸 주어지면 한번만 보면 됨)
    for c in range(M-7):
        white_start = 0 # 0,0이 흰색인 경우
        black_start = 0 # 0,0이 흑색인 경우
        for i in range(8):  # 8x8 탐색 시작
            for j in range(8):
                current = board[r+i][c+j]   # 현재 체크할 위치
                if (i + j) % 2 == 0:    # 출발점과 같은 색이여야하는 곳
                    if current != 'W':  # 검정색이면
                        white_start += 1    # 흰색에서 출발한 경우엔 +1해줘야함
                    else:
                        black_start += 1    # 흰색이면 검정색에서 출발한 경우 +1
                else:
                    if current != 'W':  # 출발점과 다른 색이여야하는 곳
                        black_start += 1    # 검정색에서 출발했는데 여기가 검정색이면 검정 출발 +1
                    else:
                        white_start += 1    # 흰색 출발했는데 여기가 흰색이면 흰색 출발 + 1
        min_cost = min(min_cost, white_start, black_start)
print(min_cost)