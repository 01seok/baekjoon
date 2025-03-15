def hanoi(n, A, B, C, moves):   # A 시작 기둥, B : C 가기전에 사용하는 보조기둥, C : 최종 도착 할 기둥
    if n == 1:  # 제일 큰 원반만 남았으면
        moves.append((A, C))  # A에서 C로 바로 이동
        return
    
    hanoi(n-1, A, C, B, moves)  # B를 보조기둥으로 사용해야하니 제일 큰 N 원반 빼고 B로 옮기기, 이 땐 C를 임시 보조 기둥으로 사용
    moves.append((A, C))        # 가장 큰 원반을 A에서  C로 이동
    hanoi(n-1, B, A, C, moves)  # B에 있던 N-1개 원반 A를 임시 보조 기둥으로 사용해서 C로 이동

N = int(input())  # 원반 개수
moves = []        # 이동 기록 저장 할 리스트

hanoi(N, 'A', 'B', 'C', moves)

print(len(moves))  # 이동 횟수
for move in moves:
    print(move[0], move[1])  # 이동 과정