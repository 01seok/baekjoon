import heapq
N = int(input())
class_lst = [tuple(map(int, input().split())) for _ in range(N)]
class_lst.sort()    # 시작 시간 기준 정렬

heap = []
heapq.heappush(heap, class_lst[0][1])   # 첫 수업 종료 시간 넣어두기(강의장 1개 사용 시작)

for i in range(1, N):
    start, end = class_lst[i]   # 이번 수업의 시작시간 종료시간

    if heap[0] <= start:    # 이번에 수업 시작하는 수업보다 이전 수업 종료시간이 빨랐다면
        heapq.heappop(heap) # 재사용 가능하니 이전 수업 제거

    heapq.heappush(heap, end)   # 강의장 재사용한다면 그 수업의 종료시간 넣어주기가 되고,
                                # 새로운 강의장 사용한다면 heap에 새 강의장 종료시간 추가해준다

# 힙에 남아있는 종료시간 개수 = 사용된 강의실 총 개수
print(len(heap))    # 필요한 강의 실 수, 재사용 가능한 강의실은 heappop으로 빼둠
