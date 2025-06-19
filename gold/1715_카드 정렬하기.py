import heapq

N = int(input())
cards = []
for _ in range(N):
    card = int(input())
    cards.append(card)
heapq.heapify(cards)    # 카드 리스트를 최소 힙으로 변경

if N == 1:
    print(0)

else:
    total = 0   # 정답 출력용(기록)

    while len(cards) > 1:
        a = heapq.heappop(cards)
        b = heapq.heappop(cards)
        s = a + b
        total += s
        heapq.heappush(cards, s)    # 남은 카드와 누적 합

    print(total)