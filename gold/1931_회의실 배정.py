N = int(input())    # 회의의 수

meeting = []    # 회의시간 담을 빈 리스트
for _ in range(N):
    start, end = map(int, input().split())  # 회의 시작시간 종료시간 입력 받기
    meeting.append((end, start))  # 회의 시간 담는데 종료 시간 기준으로 볼거니까 정렬 위해서 end부터 입력받기

meeting.sort()  # 회의 종료 시간 기준 오름차순 정렬
cnt = 0 # 정답, 회의 개수
end_time = 0    # 회의가 종료되는 시간 추가해줄 변수
for end, start in meeting:  # 시작과 종료 시간이 회의 시간 담아놓은 리스트 순회
    if start >= end_time:   # 이 때 시작 시간이 회의 종료시간보다 크다면 회의 가능
        cnt += 1
        end_time = end
print(cnt)