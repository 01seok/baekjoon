T = int(input())
for _ in range(T):
    result = input()
    
    # 연속 득점 점수와 총 점수
    continuous = 0
    total_score = 0
    
    
    for i in result:
        if i == 'O':
            # 정답을 맞춘 경우, 연속 득점 1증가하고 총 점수에 추가
            continuous += 1
            total_score += continuous
        else:
            # 틀린 경우 연속 득점 초기화
            continuous = 0
    
    print(total_score)