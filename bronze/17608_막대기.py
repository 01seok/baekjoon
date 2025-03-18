N = int(input())
sticks = [int(input()) for _ in range(N)]

cnt = 1
max_height = sticks[-1] # 제일 뒤에 있는 막대를 최대 길이로 설정

for i in range(N-2, -1, -1):  # 뒤에서 두 번째 막대기부터 탐색
    if sticks[i] > max_height:  # 현재 막대기가 더 크다면 보임
        cnt += 1
        max_height = sticks[i]  # 새로운 최대 높이 갱신

print(cnt)