N = int(input()) # 학생 수 입력
nums = list(map(int, input().split())) # 뽑은 번호 리스트로 입력

line = [] # 학생들 줄 세워서 넣을 리스트

for i in range(N):
    line.insert(i - nums[i], i+1)
    
print(*line)