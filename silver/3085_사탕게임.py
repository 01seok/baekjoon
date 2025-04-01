N = int(input())    # 배열 크기
candy_lst = [list(input()) for _ in range(N)]   # 사탕 2차원 배열

def max_candy(lst): # 자리 바꿨을 때 사탕 몇개 먹었는지 확인 할 함수
    N = len(lst)    # 배열 길이만큼 반복할거니
    max_cnt = 0
    for r in range(N):  # 가로 검사
        cnt = 1         # 1개 먹고 시작
        for c in range(N-1):    # c+1할거라 N-1까지만
            if lst[r][c] == lst[r][c+1]:    # 같으면 1개 더 먹고
                cnt += 1
            else:   # 아니면 지금까지 몇개 먹었는지 체크
                max_cnt = max(max_cnt, cnt)
                cnt = 1 # 사탕 먹은 개수 초기화
        max_cnt = max(max_cnt, cnt)

    for c in range(N):  # 세로 검사
        cnt = 1
        for r in range(N-1):
            if lst[r][c] == lst[r+1][c]:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 1
        max_cnt = max(max_cnt, cnt)

    return max_cnt

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

result = 0  # 정답, 함수 반환 값이랑 갱신해줘야 함
for r in range(N):
    for c in range(N):
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if candy_lst[r][c] != candy_lst[nr][nc]:    # 상하좌우 중 1칸 움직였을 때 다르다면
                    candy_lst[r][c], candy_lst[nr][nc] = candy_lst[nr][nc], candy_lst[r][c] # 자리 바꿔주고
                    current_result = max_candy(candy_lst)   # 함수 호출
                    result = max(result, current_result)
                    candy_lst[r][c], candy_lst[nr][nc] = candy_lst[nr][nc], candy_lst[r][c] # 다시 자리 바꾸고 탐색하러

print(result)