# 2920_음계
lst = list(map(int, input().split()))
# 8개의 숫자 리스트로 받기

if lst == list(range(1,9)):
    print('ascending') # 1~8 출력되면 어센딩 출력
    
elif lst == list(range(8, 0 ,-1)):
    print('descending') # 8 ~ 1 출력되면 디센딩
    
else: # 둘 다 아니면
    print('mixed')