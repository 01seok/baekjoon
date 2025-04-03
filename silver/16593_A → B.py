from collections import deque

A, B = map(int, input().split())    # A: 시작 숫자, B: 만들어야하는 숫자

queue = deque([(A, 1)])  # 큐 생성, 시작 숫자 A, 연산 횟수 0
# 최소 연산 값에 1을 더한 값을 출력하니 1부터 시작
result = -1 # 만들 수 없으면 -1 출력

while queue:
    current, cnt = queue.popleft()

    if current == B:
        result = cnt
        break

    if current > B:
        continue

    queue.append((current * 2, cnt + 1))
    queue.append((current * 10 + 1, cnt +1))

print(result)