A, B = map(int, input().split())

def get_position(n):
    row = (n - 1) % 4
    col = (n - 1) // 4
    return row, col

r1, c1 = get_position(A)
r2, c2 = get_position(B)

print(abs(r1 - r2) + abs(c1 - c2))