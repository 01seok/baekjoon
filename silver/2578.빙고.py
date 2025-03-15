bingo = [list(map(int, input().split())) for _ in range(5)]
call_num = [list(map(int, input().split())) for _ in range(5)]

call_list = []
for r in range(5):
    for c in range(5):
        call_list.append(call_num[r][c])  # 사회자가 부르는 숫자를 1차원 리스트로 변환

def check_bingo():
    cnt = 0
    
    # 가로 빙고 체크
    for r in range(5):
        for c in range(5):
            if bingo[r][c] != 0:
                break
        else:
            cnt += 1
    
    # 세로 빙고 체크
    for c in range(5):
        for r in range(5):
            if bingo[r][c] != 0:
                break
        else:
            cnt += 1
                
    # 왼쪽 위에서 오른쪽 아래 대각선 체크
    for i in range(5):
        if bingo[i][i] != 0:
            break
    else:
        cnt += 1
    
    # 오른쪽 위에서 왼쪽 아래 대각선 체크
    for i in range(5):
        if bingo[i][4-i] != 0:
            break
    else:
        cnt += 1
    
    return cnt

call_cnt = 0  # 부른 숫자의 개수

for num in call_list:
    call_cnt += 1
    found = False  # 숫자 찾았음을 표시하는 변수
    
    for r in range(5):
        for c in range(5):
            if bingo[r][c] == num:
                bingo[r][c] = 0
                found = True
                break  # for문 탈출
        if found:
            break
    
    if check_bingo() >= 3:
        print(call_cnt)
        break