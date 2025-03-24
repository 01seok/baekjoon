H, M = map(int, input().split())
if M >= 45:
    real_H = H
    real_M = M - 45
else:
    real_H = H - 1
    real_M = M + 15
    if real_H < 0:
        real_H = 23
        real_M = M + 15

print(real_H, real_M)