C, R = map(int, input().split())    # 가로 C, 세로 R
K = int(input())    # 어떤 관객 대기 번호

dr = [-1, 0, 1, 0]  # 상 우 하 좌 ( 문제 조건에 맞게 )
dc = [0, 1, 0, -1]
arr = [[0] * C for _ in range(R)]   # 이차원 배열 C * R
r, c, d = R-1, 0, 0 # 좌측 최하단에서 출발
num = 1 # 자리 배정 1번부터 시작
if K > C * R:
    print(0)

else:
    while num <= K: # K번째 관객 번호까지만 하면 되므로
        arr[r][c] = num
        if num == K:
            print(c + 1, R - r)
            break
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] == 0:
            r, c = nr, nc

        else:   # 다음 칸이 빈 자리가 아니라면 방향전환
            d = (d+1) % 4
            r += dr[d]
            c += dc[d]
        num += 1
