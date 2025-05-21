N = int(input())
A_lst = list(map(int, input().split()))
B_lst = list(map(int, input().split()))

A_lst.sort()
B_lst.sort(reverse=True)

result = 0
for i in range(N):
    result += A_lst[i] * B_lst[i]

print(result)