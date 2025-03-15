'''
1. 세 개의 자연수 A, B ,C 입력 받기

2. A B C 곱하기

3. 곱한 값 숫자 문자열로 변환
 
4. 문자 열로 변환한 결과 count 메서드로 빈도 세기

5. 3번 값 출력

'''

A = int(input())
B = int(input())
C = int(input())
result = A * B * C

result = str(result)

for num in range(10):
    count = result.count(str(num))
    print(count)