N = int(input())

cnt = 0
num = 666

while cnt < N:
    if '666' in str(num):
        cnt += 1
        if cnt == N:
            print(num)
            break
    num += 1