T = int(input())  # 테케 수

for _ in range(T):
    G = int(input())  # 학생 수
    student_nums = [int(input()) for _ in range(G)]

    M = 1   # 1부터 나누기 시작
    while True:
        seen = set()    # 나머지 담아둘 set, 근데 어차피 중복되면 안 넣을거지만 성능을 위해 리스트 대신 set
        for num in student_nums:    # num이 전체 학생 학번들 하나씩 가져오면서 비교
            remain = num % M
            if remain in seen:      # 봤던 나머지면 더하지 않고 다음 M 보러
                break
            seen.add(remain)        # 없던 나머지면 더해주기
        else:                       # 위 조건들 다 뚫고 모든 나머지가 다 다른 M이라면
            print(M)                # M 출력하고 종료
            break
        M += 1                      # break 걸렸을 때 or 나머지 set에 더해주고 나면 다음 M으로 나눠보기 위해 +1