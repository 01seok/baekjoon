T = int(input())

for _ in range(T):
    
    R, S = input().split() # R과 S가 공백으로 구분되어 주어지기 때문
    R = int(R) # 정수로 변환
    
    result = "" # 결과 값 문자열 담을 빈 문자열 생성
    
    for char in S:
        # 입력받는 S의 값을 char가 R번 반복
        result += char * R
    print(result)