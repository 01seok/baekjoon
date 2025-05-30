word = input().upper()  # 대소문자 통일
counter = {}

for char in word:
    if char in counter:
        counter[char] += 1
    else:
        counter[char] = 1

# 가장 많이 사용된 알파벳 찾기
max_count = max(counter.values())
max_letters = [k for k, v in counter.items() if v == max_count]

if len(max_letters) == 1:
    print(max_letters[0])
else:
    print("?")