import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
lst = list(map(int, input().split()))

lst.sort()  # 센서 위치들 오름차순 정렬

gaps = []   # 센서 간 간격들 저장할 리스트
for i in range(N-1):
    gaps.append(lst[i+1]-lst[i])

gaps.sort(reverse=True)

if K >= N:  # 1 센서 당 1 집중국 가능하니 간격 없음
    print(0)
    sys.exit()


result = sum(gaps[K-1:])    # 가장 간격 큰 K-1개 간격 합이 최소 거리
print(result)