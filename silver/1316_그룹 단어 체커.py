N = int(input())
count = 0

for _ in range(N):
    word = input()
    visited = set()
    prev = ''
    is_group = True

    for char in word:
        if char != prev:
            if char in visited:
                is_group = False
                break
            visited.add(char)
        prev = char

    if is_group:
        count += 1

print(count)