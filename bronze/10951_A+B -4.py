import sys
for line in sys.stdin:
    A, B = map(int, line.split())
    print(A+B)