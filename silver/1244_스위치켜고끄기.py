def reverse(arr, index): # 스위치 반전 함수
    arr[index] = 1 - arr[index]
    

def male(arr, num): # 남자 함수
    N = len(arr)
    for i in range(num - 1, N, num):
        reverse(arr, i)

def female(arr, num):
    N = len(arr)
    index = num - 1
    left, right = index - 1, index + 1
    
    reverse(arr, index)
    while left >= 0 and right < N and arr[left] == arr[right]:
        reverse(arr, left)
        reverse(arr, right)
        
        left -= 1
        right += 1
        
N = int(input())
arr = list(map(int, input().split()))
S = int(input())

for _ in range(S):
    gender, num = map(int, input().split())
    
    if gender == 1:
        male(arr, num)
    else:
        female(arr, num)
        
for i in range(0, N, 20):
    print(*arr[i:i+20])