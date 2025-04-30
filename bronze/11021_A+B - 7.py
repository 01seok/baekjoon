T = int(input())  # 테스트 케이스 수 입력

for tc in range(1, T + 1):
    A, B = map(int, input().split())
    print(f"Case #{tc}: {A + B}")