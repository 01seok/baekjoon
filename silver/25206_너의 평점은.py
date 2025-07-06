grade_table = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

total_score = 0.0  # 학점 * 평점
total_credit = 0.0  # P 제외 총 학점

for _ in range(20):
    subject, credit, grade = input().split()
    credit = float(credit)

    if grade == 'P':
        continue  # Pass는 계산에서 제외

    total_score += credit * grade_table[grade]
    total_credit += credit

# 전공 평점 계산 (0으로 나눌 수 있으므로 예외 처리 가능)
if total_credit == 0:
    print(0.0)
else:
    print(round(total_score / total_credit, 6))