'''
시간 초과 ver, 정답은 나옴
'''

from itertools import permutations

def base_move(bases, hit):   # 주자들이 베이스에 있을 때 관리 하는 함수
    score = 0
    # 기존 주자 이동
    # (3루 주자 확인> 2루 확인> 1루 확인)
    # 3루 홈인이면 먼저 홈인 시키면 덮어 씌울 일 없음

    for i in range(2, -1, -1):
        if bases[i]:
            new_position = i + hit
            if new_position >= 3:
                score += 1    # 홈인
            else:
                bases[new_position] = 1  # 이동
            bases[i] = 0    # 기존있던 베이스 비워주기
    # 타자 진루 또는 홈인 처리
    if hit == 4:
        score += 1        # 홈런, 타자도 홈인
    else:
        bases[hit - 1] = 1  # 1루타-1루, 2루타-2루, 3루타-3루

    return score

def baseball(lineup, innings):
    total_score = 0
    batter_idx = 0
    for inning in innings:
        base = [0, 0, 0]    # 1,2,3 루
        out_count=0
        while out_count < 3:
            hitter = lineup[batter_idx % 9]
            hit_result = inning[hitter]
            if hit_result == 0:
                out_count += 1
            else:
                total_score += base_move(base, hit_result)
            batter_idx += 1 # 다음 타자
    return total_score

N = int(input())
innings = [list(map(int, input().split())) for _ in range(N)]

# 1번 선수만 4번 타자 고정
others = list(range(1, 9))  # 8명 선수 생성
max_score = 0

for perm in permutations(others):
    lineup = list(perm[:3]) + [0] + list(perm[3:])
    real_score = baseball(lineup, innings)
    if real_score > max_score:
        max_score = real_score

print(max_score)