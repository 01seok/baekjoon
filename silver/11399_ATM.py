N = int(input())    # 사람 수
atm_lst = list(map(int, input().split()))

atm_lst.sort()
result_lst = []
time = 0

for i in range(N):
    time += atm_lst[i]
    result_lst.append(time)

print(sum(result_lst))