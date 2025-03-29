N = int(input())    # 이동해야하는 도시의 개수
distance = list(map(int, input().split()))    # 도시간 이동거리(가중치의 개념)
oil_price = list(map(int, input().split()))   # 도시 별 기름 값

min_price = oil_price[0]    # 최저가 첫번째 도시가격으로 설정 후
total_price = 0
for i in range(N-1):    # 간선 개수 만큼 반복
    if min_price > oil_price[i]:    # 이전 가격 보다 싼 곳이 있으면
        min_price = oil_price[i]    # 그 곳이 최저가
    total_price += distance[i] * min_price  # 총 비용 계산해주기
    # 더 싼 곳이 없다면 갱신될 일이 없으니 해당 주유소에서 그 만큼 넣은 것!

print(total_price)