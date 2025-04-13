for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    # 겹치는 구간이 없을 경우
    if p1 < x2 or p2 < x1 or q1 < y2 or q2 < y1:
        print('d')
    # 한 점에서 만나는 경우 (사각형 끝 모서리가 같을 경우 4가지)
    elif (p1 == x2 and q1 == y2) or (p1 == x2 and y1 == q2) or (x1 == p2 and q1 == y2) or (x1 == p2 and y1 == q2):
        print('c')
    # 선분으로 만나는 경우 두 사각형 좌 끝과 우 끝이 딱 맞고 y범위 겹칠 때
    elif (p1 == x2 or p2 == x1) and (y1 <= q2 and y2 <= q1):
        print('b')
    # 두 사각형 최상단과 최하단이 딱 맞고 x 범위가 겹칠 때
    elif (q1 == y2 or q2 == y1) and (x1 <= p2 and x2 <= p1):
        print('b')

    # 외에는 사각형 안에 사각형이 포함 되어있는 경우
    else:
        print('a')