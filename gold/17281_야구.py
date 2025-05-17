import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
innings = [list(map(int, input().split())) for _ in range(n)]
best_score = 0

# 1번 선수(인덱스 0)만 4번 타석에 고정
for perm in permutations(range(1, 9)):
    # 타순 완성: perm[:3], 1번 선수, perm[3:]
    lineup = perm[:3] + (0,) + perm[3:]
    idx = 0        # 전체 타석 인덱스
    score = 0

    for inning in innings:
        outs = 0
        first = second = third = False

        # 3아웃 될 때까지
        while outs < 3:
            res = inning[lineup[idx % 9]]
            if res == 0:
                outs += 1
            elif res == 4:
                # 홈런: 기존 주자 전원 + 타자
                score += first + second + third + 1
                first = second = third = False
            elif res == 3:
                # 3루타: 기존 주자 전원 홈인, 타자만 3루
                score += first + second + third
                first = second = False
                third = True
            elif res == 2:
                # 2루타: 2·3루 주자 홈인, 1루 주자는 3루, 타자는 2루
                score += second + third
                first, second, third = False, True, first
            else:
                # 1루타: 3루 주자 홈인, 1→2루, 2→3루, 타자→1루
                score += third
                first, second, third = True, first, second

            idx += 1

    if score > best_score:
        best_score = score

print(best_score)