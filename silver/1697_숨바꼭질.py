from collections import deque

N, K = map(int, input().split())    # 수빈이 위치, 동생 위치

queue = deque([(N, 0)]) #(덱에 출발점, 이동횟수 넣어주기)
result = 0  # 결과 값 (정답)
visited = [0] * 100001  # 방문 배열, 문제에서 0 ~ 100000

while queue:
    current, cnt = queue.popleft()  # 덱에 있는 현재 위치랑 이동 횟수 꺼내고

    if current == K:    # 현재 위치가 동생 위치면 이동 횟수 구해서 끝내기
        result = cnt
        break

    for next_node in (current-1, current+1, current * 2):   # 3가지 이동 다 고려해보기
        if 0<= next_node <= 100000 and visited[next_node] == 0: # 가보지 않은 곳이고 범위 내에 있다면
            visited[next_node] = 1  # 방문 체크하고
            queue.append((next_node, cnt + 1))  # 다음으로 이동, 이동 횟수 + 1

print(result)