T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    max_area = 0 # 사각형 최대 넓이 할당 변수
    
    for r in range(N):
        for c in range(N): # 행, 열 순회
            if arr[r][c] == 1: # 탐색하다 1을 찾으면 가로 세로 길이 구하기 시작
                width, height = 0, 0
                
                nr, nc = r, c
                while nc < N and arr[nr][nc] == 1:
                    width += 1
                    nc += 1
                    
                nr, nc = r, c    
                while nr < N and arr[nr][nc] == 1:
                    height += 1
                    nr += 1
                    
                area = width * height
                max_area = max(max_area, area)
                
                for i in range(height):
                    for j in range(width):
                        arr[r+i][c+j] = 0
                        
    print(f'#{tc} {max_area}')