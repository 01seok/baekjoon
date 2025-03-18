arr = [[0] * 100 for _ in range(100)]

for _ in range(4):
    r1, c1, r2, c2 = map(int, input().split())
    
    for r in range(c1, c2):
        for c in range(r1, r2):
            arr[r][c] = 1
            
    
cnt = 0
for r in range(100):
    for c in range(100):
        if arr[r][c] == 1:
            cnt += 1
        
print(cnt)