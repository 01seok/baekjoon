N = int(input())
arr = list(map(int, input().split())) 

max_length = 1  # 최대 길이
inc_count = 1  # 연속 증가
dec_count = 1  # 연속 감소

for i in range(1, N):
    if arr[i] > arr[i - 1]:
        inc_count += 1
        dec_count = 1  # 감소 초기화
    elif arr[i] < arr[i - 1]: 
        dec_count += 1
        inc_count = 1  # 증가 초기화
    else:  # 같은 경우
        inc_count += 1
        dec_count += 1

    max_length = max(max_length, inc_count, dec_count)

print(max_length)