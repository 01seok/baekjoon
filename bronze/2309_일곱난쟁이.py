H = [int(input()) for _ in range(9)]# 9 난쟁이의 키 리스트로 입력받기

nine_sum = sum(H) # 아홉 난쟁이 키의 합

for i in range(9):
    for j in range(i+1, 9):
        if nine_sum - (H[i] + H[j]) == 100:
            seven_dwarf = [H[k] for k in range(9) if k != i and k != j]
            seven_dwarf.sort()
            for dwarf in seven_dwarf:
                print(dwarf)
            exit()