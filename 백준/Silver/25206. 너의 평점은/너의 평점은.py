# 전공평점 = 학점 * 과목평점
# socre * A+
# 학점의 총합 sub_score
answer = 0
sub_score = 0
for i in range(20):
    S,score,grade = input().split()
    score = float(score)
    if grade != 'P':
        if grade == 'A+':
            grade = 4.5
        elif grade == 'A0':
            grade = 4.0
        elif grade == 'B+':
            grade = 3.5
        elif grade == 'B0':
            grade = 3.0
        elif grade == 'C+':
            grade = 2.5
        elif grade == 'C0':
            grade = 2.0
        elif grade == 'D+':
            grade = 1.5
        elif grade == 'D0':
            grade = 1.0
        elif grade == 'F':
            grade = 0.0
        sub_score += score
        answer += score * grade
print(answer / sub_score)

