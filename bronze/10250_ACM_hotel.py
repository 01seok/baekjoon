T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    
    r, c = 0, 0 # 위 = r , 우측 쓸 일 없음
    
    dr = (1, 0) # 위로 한칸
    
    for _ in range(1, N): # 첫 손님 이미 배정, 101호 팔려서 인덱스 1부터 시작
        nr = r + dr[0] # 위로 한칸
        nc = c + dr[1] # 좌우 이동 없음, 101호 팔렸음
        
        if nr < H:
            r, c = nr, nc
        else:
            r,c = 0, c + 1 # 꼭대기층까지 다 팔리면 다음 열로 이동
            
    room_number = f"{r + 1}{c + 1:02d}"
    print(room_number)