'''
색종이 크기 10 x 10 고정
도화지 크기 100 x 100 고정

첫번째 입력 : 색종이 개수
두번째 입력 : y축으로부터의 색종이 왼쪽 변 길이, x축으로부터의 색종이 아랫 변 길이들

구해야 하는 값 : 색종이를가 붙은 영역의 넓이를 구하기
고려할 점 : 여러개의 색종이가 붙으며 겹치는 부분의 넓이를 고려하기

'''

# 색종이 개수
N = int(input())

# 100x100 크기의 도화지
paper = [[0] * 100 for _ in range(100)]

for _ in range(N):
    r, c = map(int, input().split())  # 입력값 (r, c) → 왼쪽 아래 모서리 기준
    for i in range(10):  # 세로
        for j in range(10):  # 가로
            paper[r + i][c + j] = 1  # 색종이 있는 영역 1로 채움
            
result = 0
for row in paper:
    result += row.count(1)
        

print(result)