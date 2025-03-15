def temp_add():
    # 전체 일수 N, 합을 구할 일수 K 입력
    N, K = map(int, input().split())
    # 온도 리스트 입력
    temp = list(map(int, input().split()))
    
    # 처음 K일의 합을 계산
    current_sum = sum(temp[:K])
    max_sum = current_sum
    
    # 인덱스 K부터 N-1까지 이동하면서 합 업데이트
    for i in range(K, N):
        current_sum += temp[i] - temp[i-K]
        if current_sum > max_sum:
            max_sum = current_sum
            
    print(max_sum)