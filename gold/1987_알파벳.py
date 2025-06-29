import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = list(input() for _ in range(R))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

result = 0

def dfs(r, c, check_lst, level):
    global result

    if level > result:
        result = level

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < R and 0 <= nc < C:
            next_word = board[nr][nc]

            if next_word not in check_lst:
                check_lst.add(next_word)
                dfs(nr, nc, check_lst, level + 1)
                check_lst.remove(next_word) # 한 방향 탐색 마치고 왔을 때 check_lst 다시 지워줘야 함

check_list = {board[0][0]}
dfs(0,0, check_list, 1)
print(result)